from flask import Blueprint, render_template, request, session, redirect, url_for
from models import Pregunta, Usuario
import random

modos = Blueprint('modos_concurso', __name__)

@modos.route('/modos/concurso', methods=['GET', 'POST'])
def modo_concurso():
    niveles = [(i, f"{i}° grado") for i in range(1, 12)] + [(12, "Universidad")]
    nivel_seleccionado = session.get('concurso_nivel')
    pregunta = None
    resultado = None
    ronda = session.get('concurso_ronda', 1)
    user_obj = None

    if 'usuarioid' in session:
        user_obj = Usuario.query.get(session['usuarioid'])

    if request.method == "POST":
        # Primer ingreso: elige nivel y resetea concurso
        if "nivel" in request.form:
            nivel_seleccionado = int(request.form['nivel'])
            session['concurso_nivel'] = nivel_seleccionado
            session['concurso_ids'] = [p.id for p in Pregunta.query.filter_by(nivel=nivel_seleccionado).order_by(Pregunta.id).all()]
            random.shuffle(session['concurso_ids'])
            session['concurso_index'] = 0
            session['concurso_ronda'] = 1
        # Responde pregunta:
        elif "pregunta_id" in request.form and "opcion" in request.form:
            idx = session.get('concurso_index', 0)
            ids = session.get('concurso_ids', [])
            pregunta_actual = Pregunta.query.get(ids[idx]) if ids and idx < len(ids) else None
            if pregunta_actual and request.form['opcion'] == pregunta_actual.correcta:
                session['concurso_ronda'] += 1
                resultado = "¡Correcto! Avanzas a la siguiente ronda."
                session['concurso_index'] = idx + 1
            else:
                resultado = "¡Eliminado! Fallaste la pregunta."
                session.pop('concurso_ids', None)
                session.pop('concurso_index', None)
                session.pop('concurso_nivel', None)
                session.pop('concurso_ronda', None)

    # Mostrar pregunta:
    nivel_seleccionado = session.get('concurso_nivel')
    idx = session.get('concurso_index', 0)
    ids = session.get('concurso_ids', [])
    if ids and idx < len(ids):
        pregunta = Pregunta.query.get(ids[idx])
    elif nivel_seleccionado:
        pregunta = None

    return render_template('modos/concurso.html',
                           niveles=niveles,
                           nivel_seleccionado=nivel_seleccionado,
                           pregunta=pregunta,
                           resultado=resultado,
                           ronda=session.get('concurso_ronda', 1))
