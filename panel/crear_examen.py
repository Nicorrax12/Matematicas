from flask import Blueprint, render_template, request
from conexion import db
from models import Examen, PreguntaExamen
import random
import string

crear_examen_panel = Blueprint('crear_examen_panel', __name__, url_prefix='/panel/crear_examen')

def generar_codigo_examen():
    return ''.join(random.choices(string.digits, k=6))

@crear_examen_panel.route('/', methods=['GET', 'POST'])
def crear_examen():
    error = None
    exito = None
    codigo_examen = None
    if request.method == 'POST':
        try:
            nombre = request.form['nombre_examen']
            contrasena = request.form['contrasena']
            n_preg = int(request.form['n_preguntas'])
            codigo_examen = generar_codigo_examen()
            examen = Examen(nombre=nombre, contrasena=contrasena, codigo=codigo_examen)
            db.session.add(examen)
            db.session.commit()
            for i in range(1, n_preg + 1):
                preg = request.form.get(f'pregunta_{i}', '')
                a = request.form.get(f'opcion_a_{i}', '')
                b = request.form.get(f'opcion_b_{i}', '')
                c = request.form.get(f'opcion_c_{i}', '')
                d = request.form.get(f'opcion_d_{i}', '')
                correcta = request.form.get(f'correcta_{i}', '')
                pregunta = PreguntaExamen(
                    examen_id=examen.id, texto=preg,
                    opcion_a=a, opcion_b=b, opcion_c=c, opcion_d=d, correcta=correcta
                )
                db.session.add(pregunta)
            db.session.commit()
            exito = f"¡Examen guardado correctamente! Total preguntas: {n_preg}"
            return render_template('panel/crear_examen.html', exito=exito, error=None, codigo_examen=codigo_examen, clave_examen=contrasena)
        except Exception as e:
            db.session.rollback()
            error = f"Ocurrió un error en el guardado: {e}"
            return render_template('panel/crear_examen.html', exito=None, error=error, codigo_examen=None, clave_examen=None)
    return render_template('panel/crear_examen.html', exito=None, error=None, codigo_examen=None, clave_examen=None)
