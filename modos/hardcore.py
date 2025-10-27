from flask import Blueprint, render_template, request, session, redirect, url_for
from models import Pregunta, Usuario
from conexion import db

modos = Blueprint('modos_hardcore', __name__)

@modos.route('/modos/hardcore', methods=['GET', 'POST'])
def modo_hardcore():
    niveles = [(i, f"{i}° grado") for i in range(1, 12)] + [(12, "Universidad")]
    nivel_seleccionado = session.get('hardcore_nivel')
    pregunta = None
    resultado = None
    progreso = None
    user_obj = None
    record = None
    finalizado = False

    if 'usuarioid' in session:
        user_obj = Usuario.query.get(session['usuarioid'])
        record = user_obj.mejorracha

    if request.method == "POST":
        if "nivel" in request.form:
            nivel_seleccionado = int(request.form['nivel'])
            session['hardcore_nivel'] = nivel_seleccionado
            session['hardcore_indice'] = 0
            session['hardcore_ids'] = [p.id for p in Pregunta.query.filter_by(nivel=nivel_seleccionado).order_by(Pregunta.id).all()]
            session['hardcore_racha_actual'] = 0
        elif "pregunta_id" in request.form and "opcion" in request.form:
            progreso = session.get('hardcore_indice', 0)
            ids = session.get('hardcore_ids', [])
            pregunta_actual = Pregunta.query.get(ids[progreso]) if ids and progreso < len(ids) else None
            if pregunta_actual:
                if request.form['opcion'] == pregunta_actual.correcta:
                    resultado = "¡Correcto! 😃"
                    session['hardcore_indice'] = progreso + 1
                    session['hardcore_racha_actual'] = session.get('hardcore_racha_actual', 0) + 1
                else:
                    racha_alcanzada = session.get('hardcore_racha_actual', 0)
                    mensaje = f"¡Perdiste! Contestaste correctamente {racha_alcanzada} pregunta(s) antes de fallar."
                    # Actualiza el récord si aplica
                    if user_obj and racha_alcanzada > user_obj.mejorracha:
                        user_obj.mejorracha = racha_alcanzada
                        db.session.commit()
                        record = racha_alcanzada
                        mensaje += " ¡Nuevo récord!"
                    else:
                        record = user_obj.mejorracha
                    mensaje += f" Tu récord es {record}."
                    resultado = mensaje
                    finalizado = True
                    # Borra la sesión de modo hardcore
                    session.pop('hardcore_ids', None)
                    session.pop('hardcore_indice', None)
                    session.pop('hardcore_nivel', None)
                    session.pop('hardcore_racha_actual', None)

    nivel_seleccionado = session.get('hardcore_nivel')
    progreso = session.get('hardcore_indice', 0)
    ids = session.get('hardcore_ids', [])
    total = len(ids)
    if ids and progreso < total and not finalizado:
        pregunta = Pregunta.query.get(ids[progreso])
    elif not finalizado and nivel_seleccionado:
        resultado = "¡Completaste todas las preguntas para este nivel!"
        finalizado = True
        session.pop('hardcore_ids', None)
        session.pop('hardcore_indice', None)
        session.pop('hardcore_nivel', None)
        session.pop('hardcore_racha_actual', None)

    return render_template('modos/hardcore.html',
                           niveles=niveles,
                           nivel_seleccionado=nivel_seleccionado,
                           pregunta=pregunta,
                           resultado=resultado,
                           progreso=progreso+1 if pregunta else total,
                           total=total,
                           record=record,
                           finalizado=finalizado)
