from flask import Blueprint, render_template, request, session
from models import Pregunta, Usuario
import random
from conexion import db

modos = Blueprint('modos', __name__)

@modos.route('/modos/normal', methods=['GET', 'POST'])
def modo_normal():
    niveles = [(i, f"{i}° grado") for i in range(1, 12)] + [(12, "Universidad")]
    nivel_seleccionado = None
    pregunta = None
    resultado = None
    user_obj = None
    porcentaje = None

    if 'usuarioid' in session:
        user_obj = Usuario.query.get(session['usuarioid'])
        rachaactual = user_obj.rachaactual
        mejorracha = user_obj.mejorracha
        preguntas_acertadas = user_obj.preguntas_acertadas
        preguntas_total = user_obj.preguntas_total
        if preguntas_total > 0:
            porcentaje = round(100 * preguntas_acertadas / preguntas_total)
        else:
            porcentaje = 0
    else:
        # Usuario no loggeado
        rachaactual = mejorracha = preguntas_acertadas = preguntas_total = porcentaje = None

    if request.method == 'POST':
        nivel_seleccionado = int(request.form.get('nivel', 1))
        preguntas = Pregunta.query.filter_by(nivel=nivel_seleccionado).all()
        if preguntas:
            pregunta_id = request.form.get('pregunta_id')
            respuesta_usuario = request.form.get('opcion')
            pregunta_actual = None
            if pregunta_id:
                pregunta_actual = next((p for p in preguntas if str(p.id) == pregunta_id), None)
                if pregunta_actual and respuesta_usuario and user_obj:
                    user_obj.preguntas_total += 1
                    if respuesta_usuario == pregunta_actual.correcta:
                        resultado = "¡Correcto! 😃"
                        user_obj.rachaactual += 1
                        user_obj.preguntas_acertadas += 1
                        if user_obj.rachaactual > user_obj.mejorracha:
                            user_obj.mejorracha = user_obj.rachaactual
                    else:
                        resultado = f"Incorrecto. La respuesta era {pregunta_actual.correcta.upper()}."
                        user_obj.rachaactual = 0
                    db.session.commit()
                    # Actualizar los stats recién modificados
                    preguntas_acertadas = user_obj.preguntas_acertadas
                    preguntas_total = user_obj.preguntas_total
                    rachaactual = user_obj.rachaactual
                    mejorracha = user_obj.mejorracha
                    if preguntas_total > 0:
                        porcentaje = round(100 * preguntas_acertadas / preguntas_total)
                    else:
                        porcentaje = 0
            pregunta = random.choice(preguntas)
        else:
            resultado = "No hay preguntas para este nivel."
    return render_template('modos/normal.html',
                           niveles=niveles,
                           nivel_seleccionado=nivel_seleccionado,
                           pregunta=pregunta,
                           resultado=resultado,
                           rachaactual=rachaactual,
                           mejorracha=mejorracha,
                           porcentaje=porcentaje)
