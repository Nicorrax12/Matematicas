"""

UNIPAZ Quiz System - Backend Flask Completo

Conecta a: unipaz_db | Usuario: root | Contraseña: 1606

CON AUTENTICACIÓN, LOGIN Y REGISTRO FUNCIONALES

ACTUALIZADO: 2025-11-10 - RUTAS CORREGIDAS + IMPORT BACKEND ROUTES

"""

import os
import hashlib
import secrets
import sys
from datetime import timedelta
from pathlib import Path
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv


# Cargar variables de entorno
load_dotenv()


# ===== INICIALIZAR FLASK =====
app = Flask(__name__,
    template_folder='templates',
    static_folder='static'
)


# ===== CONFIGURACIÓN =====
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1606@localhost:3306/unipaz_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['JSON_SORT_KEYS'] = False


# ===== INICIALIZAR EXTENSIONES =====
db = SQLAlchemy(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})


# ===== MODELOS =====


class Carrera(db.Model):
    __tablename__ = 'carreras'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    icono = db.Column(db.String(50))
    color = db.Column(db.String(7))


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    carrera_id = db.Column(db.Integer, db.ForeignKey('carreras.id'))
    racha_actual = db.Column(db.Integer, default=0)
    racha_maxima = db.Column(db.Integer, default=0)
    total_puntos = db.Column(db.Integer, default=0)
    preguntas_correctas = db.Column(db.Integer, default=0)
    preguntas_totales = db.Column(db.Integer, default=0)


class Materia(db.Model):
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    carrera_id = db.Column(db.Integer, db.ForeignKey('carreras.id'), nullable=False)
    semestre = db.Column(db.Integer)
    profesor = db.Column(db.String(150))
    descripcion = db.Column(db.Text)


class Pregunta(db.Model):
    __tablename__ = 'preguntas'
    id = db.Column(db.Integer, primary_key=True)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    opcion_a = db.Column(db.String(500))
    opcion_b = db.Column(db.String(500))
    opcion_c = db.Column(db.String(500))
    opcion_d = db.Column(db.String(500))
    respuesta_correcta = db.Column(db.String(1))
    dificultad = db.Column(db.String(20), default='medio')
    activo = db.Column(db.Boolean, default=True)


class Examen(db.Model):
    __tablename__ = 'examenes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    creado_por = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    descripcion = db.Column(db.Text)
    duracion_minutos = db.Column(db.Integer, default=60)
    contraseña = db.Column(db.String(100))
    codigo_acceso = db.Column(db.String(50), unique=True, nullable=True)
    permitir_repaso = db.Column(db.Boolean, default=True)
    mostrar_puntaje_inmediato = db.Column(db.Boolean, default=True)
    permitir_volver_atras = db.Column(db.Boolean, default=True)
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=db.func.now())


# ===== TABLA INTERMEDIA PARA EXAMEN-PREGUNTA =====
class ExamenPregunta(db.Model):
    __tablename__ = 'examen_preguntas'
    id = db.Column(db.Integer, primary_key=True)
    examen_id = db.Column(db.Integer, db.ForeignKey('examenes.id'), nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('preguntas.id'), nullable=False)
    orden = db.Column(db.Integer, default=0)
    puntos = db.Column(db.Integer, default=1)


# ===== FUNCIONES AUXILIARES =====


def hashear_password(password):
    """Hashear contraseña"""
    return hashlib.sha256(password.encode()).hexdigest()


def verificar_password(password, password_hash):
    """Verificar contraseña"""
    return hashear_password(password) == password_hash


# ===== RUTAS FRONTEND =====


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/login')
def login():
    """Login page"""
    return render_template('login.html')


@app.route('/registro')
def registro():
    """Registro page"""
    return render_template('registro.html')


@app.route('/quiz')
def quiz():
    """Quiz page"""
    return render_template('quiz.html')


@app.route('/rankings')
def rankings():
    """Rankings page"""
    return render_template('rankings.html')


@app.route('/concursos')
def concursos():
    """Concursos page"""
    return render_template('concursos.html')


@app.route('/dashboard')
def dashboard():
    """Dashboard page"""
    return render_template('dashboard.html')


@app.route('/crear-examen')
def crear_examen_page():
    """Página para crear examen"""
    return render_template('crear-examen.html')


@app.route('/unirse-examen')
def unirse_examen_page():
    """Página para unirse a examen"""
    return render_template('unirse-examen.html')


@app.route('/debug-examen')
def debug_examen():
    """Página de debug para unirse a examen"""
    return render_template('debug-examen.html')


@app.route('/examen/<int:examen_id>')
def ver_examen(examen_id):
    """Página para responder examen"""
    return render_template('responder-examen.html', examen_id=examen_id)


# ===== RUTAS API - AUTENTICACIÓN =====


@app.route('/api/login', methods=['POST'])
def api_login():
    """Endpoint para login"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email y contraseña requeridos'}), 400

        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario or not verificar_password(password, usuario.password_hash):
            return jsonify({'error': 'Email o contraseña incorrectos'}), 401

        return jsonify({
            'success': True,
            'usuario': {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'email': usuario.email,
                'carrera_id': usuario.carrera_id
            }
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/register', methods=['POST'])
def api_register():
    """Endpoint para registro"""
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        email = data.get('email')
        password = data.get('password')
        carrera_id = data.get('carrera_id')

        if not all([nombre, email, password, carrera_id]):
            return jsonify({'error': 'Todos los campos son requeridos'}), 400

        if Usuario.query.filter_by(email=email).first():
            return jsonify({'error': 'El email ya está registrado'}), 409

        nuevo_usuario = Usuario(
            nombre=nombre,
            email=email,
            password_hash=hashear_password(password),
            carrera_id=carrera_id
        )

        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Usuario registrado exitosamente',
            'usuario': {
                'id': nuevo_usuario.id,
                'nombre': nuevo_usuario.nombre,
                'email': nuevo_usuario.email
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ===== RUTAS API - CARRERAS =====


@app.route('/api/carreras', methods=['GET'])
def get_carreras():
    """Obtener todas las carreras"""
    try:
        carreras = Carrera.query.all()
        resultado = [{
            'id': c.id,
            'nombre': c.nombre,
            'icono': c.icono,
            'color': c.color,
            'descripcion': c.descripcion
        } for c in carreras]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ===== RUTAS API - MATERIAS =====


@app.route('/api/materias', methods=['GET'])
def get_materias():
    """Obtener todas las materias"""
    try:
        materias = Materia.query.all()
        resultado = [{
            'id': m.id,
            'nombre': m.nombre,
            'carrera_id': m.carrera_id,
            'semestre': m.semestre,
            'profesor': m.profesor,
            'descripcion': m.descripcion
        } for m in materias]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/materias/carrera/<int:carrera_id>', methods=['GET'])
def get_materias_por_carrera(carrera_id):
    """Obtener materias de una carrera específica - CORREGIDO CON PARAMETRO"""
    try:
        materias = Materia.query.filter_by(carrera_id=carrera_id).order_by(Materia.semestre).all()
        resultado = [{
            'id': m.id,
            'nombre': m.nombre,
            'carrera_id': m.carrera_id,
            'semestre': m.semestre,
            'profesor': m.profesor,
            'descripcion': m.descripcion
        } for m in materias]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ===== RUTAS API - PREGUNTAS =====


@app.route('/api/quiz/preguntas/<int:materia_id>', methods=['GET'])
def get_preguntas(materia_id):
    """Obtener preguntas de una materia - CORREGIDO CON PARAMETRO"""
    try:
        dificultad = request.args.get('dificultad', 'medio')
        cantidad = request.args.get('cantidad', 10, type=int)

        preguntas = Pregunta.query.filter_by(
            materia_id=materia_id,
            dificultad=dificultad,
            activo=True
        ).limit(cantidad).all()

        if not preguntas:
            preguntas = Pregunta.query.filter_by(
                materia_id=materia_id,
                activo=True
            ).limit(cantidad).all()

        resultado = [{
            'id': p.id,
            'texto': p.texto,
            'opciones': {
                'a': p.opcion_a,
                'b': p.opcion_b,
                'c': p.opcion_c,
                'd': p.opcion_d
            },
            'respuesta_correcta': p.respuesta_correcta,
            'dificultad': p.dificultad
        } for p in preguntas]

        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ===== RUTAS API - EXAMENES =====


@app.route('/api/examenes/crear', methods=['POST'])
def crear_examen_api():
    """Crear un examen"""
    try:
        data = request.json
        if not data.get('nombre') or not data.get('materia_id'):
            return jsonify({'error': 'Nombre y materia son requeridos'}), 400

        codigo_acceso = secrets.token_hex(6).upper()
        while Examen.query.filter_by(codigo_acceso=codigo_acceso).first():
            codigo_acceso = secrets.token_hex(6).upper()

        nuevo_examen = Examen(
            nombre=data['nombre'],
            materia_id=data['materia_id'],
            creado_por=data.get('creado_por'),
            descripcion=data.get('descripcion', ''),
            duracion_minutos=data.get('duracion_minutos', 60),
            contraseña=data.get('contraseña', None),
            codigo_acceso=codigo_acceso
        )

        db.session.add(nuevo_examen)
        db.session.commit()

        return jsonify({
            'examen_id': nuevo_examen.id,
            'codigo_acceso': codigo_acceso,
            'mensaje': 'Examen creado exitosamente'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/api/examenes/<int:examen_id>/preguntas', methods=['POST'])
def agregar_pregunta(examen_id):
    """Agregar una pregunta a un examen"""
    try:
        data = request.json
        
        examen = Examen.query.get(examen_id)
        if not examen:
            return jsonify({'error': 'Examen no encontrado'}), 404
        
        if not all(k in data for k in ['materia_id', 'texto', 'opcion_a', 'opcion_b', 'opcion_c', 'opcion_d', 'respuesta_correcta']):
            return jsonify({'error': 'Faltan campos requeridos'}), 400

        nueva_pregunta = Pregunta(
            materia_id=data['materia_id'],
            texto=data['texto'],
            opcion_a=data['opcion_a'],
            opcion_b=data['opcion_b'],
            opcion_c=data['opcion_c'],
            opcion_d=data['opcion_d'],
            respuesta_correcta=data['respuesta_correcta'],
            dificultad=data.get('dificultad', 'medio'),
            activo=True
        )

        db.session.add(nueva_pregunta)
        db.session.flush()

        examen_pregunta = ExamenPregunta(
            examen_id=examen_id,
            pregunta_id=nueva_pregunta.id,
            orden=0,
            puntos=1
        )

        db.session.add(examen_pregunta)
        db.session.commit()

        return jsonify({
            'pregunta_id': nueva_pregunta.id,
            'mensaje': 'Pregunta agregada exitosamente'
        }), 201
    except Exception as e:
        db.session.rollback()
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500


@app.route('/api/examenes/<int:examen_id>/preguntas', methods=['GET'])
def obtener_preguntas_examen(examen_id):
    """Obtener preguntas de un examen"""
    try:
        examen = Examen.query.get(examen_id)
        if not examen:
            return jsonify({'error': 'Examen no encontrado'}), 404
        
        preguntas_rel = ExamenPregunta.query.filter_by(examen_id=examen_id)\
            .order_by(ExamenPregunta.orden).all()
        
        resultado = []
        
        for rel in preguntas_rel:
            pregunta = Pregunta.query.get(rel.pregunta_id)
            if pregunta:
                resultado.append({
                    'id': pregunta.id,
                    'texto': pregunta.texto,
                    'opcion_a': pregunta.opcion_a if pregunta.opcion_a else '',
                    'opcion_b': pregunta.opcion_b if pregunta.opcion_b else '',
                    'opcion_c': pregunta.opcion_c if pregunta.opcion_c else '',
                    'opcion_d': pregunta.opcion_d if pregunta.opcion_d else '',
                    'respuesta_correcta': pregunta.respuesta_correcta
                })
        
        return jsonify(resultado), 200
        
    except Exception as e:
        print(f'Error: {str(e)}')
        return jsonify({'error': str(e)}), 500


@app.route('/api/examenes/buscar-por-codigo', methods=['POST'])
def buscar_examen_codigo():
    """Buscar examen por código de acceso"""
    try:
        data = request.json
        codigo = data.get('codigo_acceso', '').upper()

        if not codigo:
            return jsonify({'error': 'Código de acceso requerido'}), 400

        examen = Examen.query.filter_by(codigo_acceso=codigo, activo=True).first()

        if not examen:
            return jsonify({'error': 'Código de acceso no encontrado'}), 404

        return jsonify({
            'examen_id': examen.id,
            'nombre': examen.nombre,
            'materia_id': examen.materia_id,
            'duracion': examen.duracion_minutos,
            'tiene_contraseña': examen.contraseña is not None
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/examenes/<int:examen_id>', methods=['GET'])
def obtener_examen(examen_id):
    """Obtener detalles de un examen"""
    try:
        examen = Examen.query.get(examen_id)
        if not examen:
            return jsonify({'error': 'Examen no encontrado'}), 404

        preguntas_rel = ExamenPregunta.query.filter_by(examen_id=examen_id).all()

        return jsonify({
            'id': examen.id,
            'nombre': examen.nombre,
            'materia_id': examen.materia_id,
            'descripcion': examen.descripcion,
            'duracion_minutos': examen.duracion_minutos,
            'num_preguntas': len(preguntas_rel),
            'permitir_repaso': examen.permitir_repaso,
            'mostrar_puntaje_inmediato': examen.mostrar_puntaje_inmediato
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ===== RUTAS API - RANKINGS =====


@app.route('/api/rankings/global/racha', methods=['GET'])
def rankings_racha():
    """Top 10 mejores rachas"""
    try:
        usuarios = Usuario.query.order_by(Usuario.racha_actual.desc()).limit(10).all()
        resultado = [{
            'posicion': idx + 1,
            'nombre': u.nombre,
            'racha': u.racha_actual,
            'puntos': u.total_puntos
        } for idx, u in enumerate(usuarios)]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ===== HEALTH CHECK =====


@app.route('/api/health', methods=['GET'])
def health():
    """Verificar conexión a BD"""
    try:
        db.session.execute('SELECT 1')
        return jsonify({
            'status': 'ok',
            'database': 'connected',
            'message': '✅ Conexión a unipaz_db exitosa'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'database': 'disconnected',
            'message': f'❌ Error: {str(e)}'
        }), 500


# ===== ERROR HANDLERS =====


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Recurso no encontrado'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Error del servidor'}), 500


# ===== IMPORTAR ROUTES DESDE BACKEND =====

try:
    # Agregar la carpeta backend al path de Python
    backend_path = Path(__file__).parent / 'backend'
    sys.path.insert(0, str(backend_path))
    
    # Importar routes
    from routes import registrar_rutas
    registrar_rutas(app)
    print("✅ Routes desde backend importadas correctamente")
except ImportError as e:
    print(f"⚠️ Advertencia: No se pudieron importar las routes desde backend: {e}")


# ===== MAIN =====


if __name__ == '__main__':
    with app.app_context():
        print("=" * 60)
        print("🚀 UNIPAZ QUIZ SYSTEM - Backend")
        print("=" * 60)
        print("📊 Base de Datos: unipaz_db")
        print("👤 Usuario: root")
        print("🔐 Contraseña: 1606")
        print("=" * 60)

        try:
            db.create_all()
            print("✅ Tablas de BD verificadas")
        except Exception as e:
            print(f"❌ Error con BD: {str(e)}")

        print("=" * 60)
        print("🌍 Iniciando servidor en http://localhost:5000")
        print("=" * 60)
        print("\n✅ RUTAS DISPONIBLES:")
        print(" GET / - Home")
        print(" GET /login - Login")
        print(" GET /registro - Registro")
        print(" GET /quiz - Quiz")
        print(" GET /rankings - Rankings")
        print(" GET /api/health - Health Check")
        print("\n")

        app.run(debug=True, host='0.0.0.0', port=5000)