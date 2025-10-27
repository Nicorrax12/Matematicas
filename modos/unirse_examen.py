from flask import Blueprint, render_template, request, session
from conexion import db
from models import Examen, PreguntaExamen
from datetime import datetime

unirse_examen_panel = Blueprint('unirse_examen_panel', __name__, url_prefix='/unirse_examen')

@unirse_examen_panel.route('/', methods=['GET', 'POST'])
def unirse():
    if request.method == 'POST' and 'codigo' in request.form:
        codigo = request.form['codigo']
        contrasena = request.form['contrasena']
        usuario = request.form['usuario']
        examen = Examen.query.filter_by(codigo=codigo, contrasena=contrasena).first()
        if not examen:
            return render_template('modos/unirse_examen.html', error="Código o contraseña inválidos", respondido=False)
        preguntas = PreguntaExamen.query.filter_by(examen_id=examen.id).all()
        session['inicio_exam'] = datetime.utcnow().isoformat()
        return render_template('modos/unirse_examen.html', error=None, respondido=False,
                               examen=examen, preguntas=preguntas, usuario=usuario)
    return render_template('modos/unirse_examen.html', error=None, respondido=False)

@unirse_examen_panel.route('/responder', methods=['POST'])
def responder():
    usuario = request.form['usuario']
    examen_id = request.form['examen_id']
    examen = Examen.query.get(examen_id)
    preguntas = PreguntaExamen.query.filter_by(examen_id=examen.id).all()
    puntaje = 0
    for p in preguntas:
        r = request.form.get(f'pregunta_{p.id}')
        if r and r.lower() == p.correcta.lower():
            puntaje += 1
    total = len(preguntas)
    inicio = datetime.fromisoformat(session.get('inicio_exam'))
    tiempo = int((datetime.utcnow() - inicio).total_seconds())
    return render_template('modos/unirse_examen.html', respondido=True, examen=examen, preguntas=preguntas,
                           usuario=usuario, puntaje=puntaje, total=total, tiempo=tiempo)
