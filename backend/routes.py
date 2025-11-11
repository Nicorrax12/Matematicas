# backend/routes.py - Rutas del Backend Flask COMPLETO Y CORREGIDO

from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from app import db
import random
import string


# ========== BLUEPRINTS ==========


rankigns_bp = Blueprint('rankings', __name__, url_prefix='/api/rankings')
quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quiz')
usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/api/usuarios')
api_bp = Blueprint('api', __name__, url_prefix='/api')  # Para examenes


# ========== MATERIAS ==========


@api_bp.route('/materias', methods=['GET'])
def obtener_materias():
    try:
        from app import Materia
        materias = Materia.query.filter_by(activo=True).order_by(Materia.nombre).all()
        return jsonify([{'id': m.id, 'nombre': m.nombre} for m in materias]), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ========== CREAR EXAMEN ==========


@api_bp.route('/examenes/crear', methods=['POST'])
def crear_examen():
    data = request.get_json()
    
    try:
        from app import Examen
        
        # Generar código de acceso
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        
        # Crear examen
        examen = Examen(
            materia_id=data['materia_id'],
            nombre=data['nombre'],
            duracion_minutos=data['duracion_minutos'],
            contraseña=data.get('contraseña'),
            codigo_acceso=codigo,
            activo=True
        )
        
        db.session.add(examen)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'examen_id': examen.id,
            'codigo_acceso': codigo
        }), 200
    except Exception as e:
        db.session.rollback()
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ========== CREAR PREGUNTA ==========


@api_bp.route('/examenes/<int:examen_id>/preguntas', methods=['POST'])
def crear_pregunta(examen_id):
    data = request.get_json()
    
    try:
        from app import Pregunta, Examen, ExamenPregunta
        
        # Validar que el examen exista
        examen = Examen.query.get(examen_id)
        if not examen:
            return jsonify({'error': 'Examen no encontrado'}), 404
        
        # 1. Crear la pregunta en tabla preguntas
        # IMPORTANTE: usar materia_id del payload
        pregunta = Pregunta(
            materia_id=data['materia_id'],
            texto=data['texto'],
            opcion_a=data['opcion_a'],
            opcion_b=data['opcion_b'],
            opcion_c=data['opcion_c'],
            opcion_d=data['opcion_d'],
            respuesta_correcta=data['respuesta_correcta'],
            activo=True
        )
        
        db.session.add(pregunta)
        db.session.flush()  # Para obtener el ID sin hacer commit
        
        # 2. Asociar pregunta al examen en tabla examen_preguntas
        examen_pregunta = ExamenPregunta(
            examen_id=examen_id,
            pregunta_id=pregunta.id,
            orden=0,
            puntos=1
        )
        
        db.session.add(examen_pregunta)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'pregunta_id': pregunta.id,
            'examen_id': examen_id
        }), 200
    except Exception as e:
        db.session.rollback()
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ========== OBTENER EXAMEN ==========


@api_bp.route('/examenes/<int:examen_id>', methods=['GET'])
def obtener_examen(examen_id):
    try:
        from app import Examen
        
        examen = Examen.query.get(examen_id)
        if not examen:
            return jsonify({'error': 'Examen no encontrado'}), 404
        
        return jsonify({
            'id': examen.id,
            'materia_id': examen.materia_id,
            'nombre': examen.nombre,
            'duracion_minutos': examen.duracion_minutos,
            'codigo_acceso': examen.codigo_acceso,
            'activo': examen.activo
        }), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ========== OBTENER PREGUNTAS DEL EXAMEN ==========


@api_bp.route('/examenes/<int:examen_id>/preguntas', methods=['GET'])
def obtener_preguntas_examen(examen_id):
    try:
        from app import Pregunta, ExamenPregunta
        
        preguntas_rel = ExamenPregunta.query.filter_by(examen_id=examen_id)\
            .order_by(ExamenPregunta.orden).all()
        
        resultado = []
        for rel in preguntas_rel:
            p = rel.pregunta
            resultado.append({
                'id': p.id,
                'texto': p.texto,
                'opcion_a': p.opcion_a,
                'opcion_b': p.opcion_b,
                'opcion_c': p.opcion_c,
                'opcion_d': p.opcion_d,
                'respuesta_correcta': p.respuesta_correcta
            })
        
        return jsonify(resultado), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ===== RANKINGS =====


@rankigns_bp.route('/global/racha', methods=['GET'])
def ranking_racha_global():
    """Top 10 mejores rachas global"""
    try:
        from app import Usuario
        
        usuarios = Usuario.query.order_by(Usuario.racha_actual.desc()).limit(10).all()
        resultado = []
        
        for idx, usuario in enumerate(usuarios, 1):
            resultado.append({
                'posicion': idx,
                'id': usuario.id,
                'nombre': usuario.nombre,
                'avatar': usuario.avatar,
                'carrera': usuario.carrera.nombre if usuario.carrera else 'Sin carrera',
                'racha': usuario.racha_actual,
                'puntos': usuario.total_puntos,
                'porcentaje': usuario.porcentaje_exito
            })
        
        return jsonify(resultado), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



@rankigns_bp.route('/global/porcentaje', methods=['GET'])
def ranking_porcentaje_global():
    """Top 10 mejor porcentaje de éxito global"""
    try:
        from app import Usuario
        
        usuarios = Usuario.query.filter(Usuario.preguntas_totales > 0)\
            .order_by((Usuario.preguntas_correctas / Usuario.preguntas_totales).desc())\
            .limit(10).all()
        
        resultado = []
        for idx, usuario in enumerate(usuarios, 1):
            resultado.append({
                'posicion': idx,
                'id': usuario.id,
                'nombre': usuario.nombre,
                'avatar': usuario.avatar,
                'carrera': usuario.carrera.nombre if usuario.carrera else 'Sin carrera',
                'porcentaje': usuario.porcentaje_exito,
                'preguntas_correctas': usuario.preguntas_correctas,
                'preguntas_totales': usuario.preguntas_totales
            })
        
        return jsonify(resultado), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



@rankigns_bp.route('/materia/<int:materia_id>/racha', methods=['GET'])
def ranking_racha_materia(materia_id):
    """Top 10 rachas por materia"""
    try:
        from app import Usuario, Ranking
        
        rankings = Ranking.query.filter_by(
            materia_id=materia_id,
            tipo='racha',
            periodo='global'
        ).order_by(Ranking.valor.desc()).limit(10).all()
        
        resultado = []
        for ranking in rankings:
            usuario = Usuario.query.get(ranking.usuario_id)
            resultado.append({
                'posicion': ranking.posicion,
                'id': usuario.id,
                'nombre': usuario.nombre,
                'avatar': usuario.avatar,
                'racha': ranking.valor,
                'puntos': usuario.total_puntos
            })
        
        return jsonify(resultado), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ===== QUIZ =====


@quiz_bp.route('/preguntas/<int:materia_id>', methods=['GET'])
def get_preguntas(materia_id):
    """Obtener preguntas de una materia"""
    try:
        from app import Pregunta
        
        dificultad = request.args.get('dificultad', 'medio')
        cantidad = request.args.get('cantidad', 10, type=int)
        
        preguntas = Pregunta.query.filter_by(
            materia_id=materia_id,
            dificultad=dificultad,
            activo=True
        ).limit(cantidad).all()
        
        resultado = []
        for pregunta in preguntas:
            resultado.append({
                'id': pregunta.id,
                'texto': pregunta.texto,
                'opciones': {
                    'a': pregunta.opcion_a,
                    'b': pregunta.opcion_b,
                    'c': pregunta.opcion_c,
                    'd': pregunta.opcion_d
                },
                'dificultad': pregunta.dificultad,
                'imagen': pregunta.imagen_url
            })
        
        return jsonify(resultado), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



@quiz_bp.route('/responder', methods=['POST'])
def responder_pregunta():
    """Registrar respuesta de usuario"""
    try:
        from app import Respuesta, Pregunta, Usuario
        
        data = request.get_json()
        
        # Validar datos
        if not all(k in data for k in ['usuario_id', 'pregunta_id', 'respuesta_dada']):
            return jsonify({'error': 'Datos incompletos'}), 400
        
        # Obtener pregunta
        pregunta = Pregunta.query.get(data['pregunta_id'])
        if not pregunta:
            return jsonify({'error': 'Pregunta no encontrada'}), 404
        
        # Validar respuesta
        es_correcta = data['respuesta_dada'].upper() == pregunta.respuesta_correcta
        
        # Registrar respuesta
        respuesta = Respuesta(
            usuario_id=data['usuario_id'],
            pregunta_id=data['pregunta_id'],
            respuesta_dada=data['respuesta_dada'],
            es_correcta=es_correcta,
            tiempo_respuesta=data.get('tiempo_respuesta', 0),
            modo=data.get('modo', 'normal'),
            materia_id=pregunta.materia_id
        )
        
        db.session.add(respuesta)
        
        # Actualizar estadísticas del usuario
        usuario = Usuario.query.get(data['usuario_id'])
        usuario.preguntas_totales += 1
        
        if es_correcta:
            usuario.preguntas_correctas += 1
            usuario.racha_actual += 1
            usuario.total_puntos += 10
            
            # Actualizar racha máxima
            if usuario.racha_actual > usuario.racha_maxima:
                usuario.racha_maxima = usuario.racha_actual
        else:
            usuario.racha_actual = 0
        
        db.session.commit()
        
        return jsonify({
            'correcta': es_correcta,
            'respuesta_correcta': pregunta.respuesta_correcta,
            'explicacion': pregunta.explicacion,
            'puntos_ganados': 10 if es_correcta else 0
        }), 200
    except Exception as e:
        db.session.rollback()
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



@quiz_bp.route('/siguiente', methods=['GET'])
def siguiente_pregunta():
    """Obtener siguiente pregunta aleatoria"""
    try:
        from app import Pregunta
        
        materia_id = request.args.get('materia_id', type=int)
        dificultad = request.args.get('dificultad', 'medio')
        
        preguntas = Pregunta.query.filter_by(
            materia_id=materia_id,
            dificultad=dificultad,
            activo=True
        ).all()
        
        if not preguntas:
            return jsonify({'error': 'No hay preguntas disponibles'}), 404
        
        pregunta = random.choice(preguntas)
        
        return jsonify({
            'id': pregunta.id,
            'texto': pregunta.texto,
            'opciones': {
                'a': pregunta.opcion_a,
                'b': pregunta.opcion_b,
                'c': pregunta.opcion_c,
                'd': pregunta.opcion_d
            },
            'dificultad': pregunta.dificultad,
            'imagen': pregunta.imagen_url
        }), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ===== USUARIOS =====


@usuarios_bp.route('/<int:usuario_id>/estadisticas', methods=['GET'])
def estadisticas_usuario(usuario_id):
    """Obtener estadísticas del usuario"""
    try:
        from app import Usuario, Respuesta
        
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        # Respuestas últimos 7 días
        hace_7_dias = datetime.utcnow() - timedelta(days=7)
        respuestas_semana = Respuesta.query.filter(
            Respuesta.usuario_id == usuario_id,
            Respuesta.fecha_respuesta >= hace_7_dias
        ).all()
        
        correctas_semana = sum(1 for r in respuestas_semana if r.es_correcta)
        
        return jsonify({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'nivel': usuario.nivel,
            'xp': usuario.xp,
            'racha_actual': usuario.racha_actual,
            'racha_maxima': usuario.racha_maxima,
            'total_puntos': usuario.total_puntos,
            'porcentaje_exito': usuario.porcentaje_exito,
            'preguntas_correctas': usuario.preguntas_correctas,
            'preguntas_totales': usuario.preguntas_totales,
            'respuestas_semana': len(respuestas_semana),
            'correctas_semana': correctas_semana,
            'fecha_creacion': usuario.fecha_creacion.isoformat()
        }), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



@usuarios_bp.route('/<int:usuario_id>/historial', methods=['GET'])
def historial_usuario(usuario_id):
    """Obtener historial de respuestas"""
    try:
        from app import Respuesta, Pregunta
        
        limite = request.args.get('limite', 20, type=int)
        respuestas = Respuesta.query.filter_by(usuario_id=usuario_id)\
            .order_by(Respuesta.fecha_respuesta.desc())\
            .limit(limite).all()
        
        resultado = []
        for respuesta in respuestas:
            pregunta = Pregunta.query.get(respuesta.pregunta_id)
            resultado.append({
                'id': respuesta.id,
                'pregunta': pregunta.texto,
                'respuesta_dada': respuesta.respuesta_dada,
                'correcta': respuesta.es_correcta,
                'tiempo': respuesta.tiempo_respuesta,
                'fecha': respuesta.fecha_respuesta.isoformat()
            })
        
        return jsonify(resultado), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ===== SALUD =====


@usuarios_bp.route('/salud', methods=['GET'])
def salud_api():
    """Endpoint de salud de la API"""
    return jsonify({
        'estado': 'ok',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    }), 200



# ========== REGISTRAR BLUEPRINTS ==========


def registrar_rutas(app):
    """Función para registrar todos los blueprints en app.py"""
    app.register_blueprint(rankigns_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(api_bp)