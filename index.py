import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # ¡Permite imports de subcarpetas!

from flask import Flask, render_template, redirect, url_for, session, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from conexion import db, init_db
from models import Usuario

from modos.normal import modos as normal_modos
from modos.hardcore import modos as hardcore_modos
from modos.concurso import modos as concurso_modos
from modos.unirse_examen import unirse_examen_panel
from panel.crear_examen import crear_examen_panel  # ESTE IMPORT DEBE FUNCIONAR
app = Flask(__name__)
app.secret_key = 'clave-cualquiera'
init_db(app)

app.register_blueprint(normal_modos)
app.register_blueprint(hardcore_modos)
app.register_blueprint(concurso_modos)
app.register_blueprint(unirse_examen_panel)
app.register_blueprint(crear_examen_panel)

@app.route('/')
def index():
    isLogged = 'usuarioid' in session
    nombre = session.get('nombre', 'Invitado')
    return render_template('index.html', isLogged=isLogged, nombre=nombre)

@app.route('/usuario/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        contrasena = request.form.get('contrasena', '')
        if not email or not contrasena:
            error = 'Todos los campos son obligatorios.'
        else:
            user = Usuario.query.filter_by(email=email).first()
            if user and check_password_hash(user.contrasena, contrasena):
                session['usuarioid'] = user.id
                session['nombre'] = user.nombre
                session['email'] = user.email
                return redirect(url_for('index'))
            else:
                error = 'Email o contraseña incorrectos.'
    return render_template('usuario/login.html', error=error)

@app.route('/usuario/registro', methods=['GET', 'POST'])
def registro():
    error = ''
    if request.method == 'POST':
        nombre = request.form.get('nombre','').strip()
        email = request.form.get('email','').strip()
        contrasena = request.form.get('contrasena', '')
        confirmar = request.form.get('confirmar', '')
        if not nombre or not email or not contrasena or not confirmar:
            error = 'Todos los campos son obligatorios.'
        elif contrasena != confirmar:
            error = 'Las contraseñas no coinciden.'
        elif Usuario.query.filter_by(email=email).first():
            error = 'Ya existe una cuenta con ese correo.'
        else:
            hash_password = generate_password_hash(contrasena)
            nuevo = Usuario(nombre=nombre, email=email, contrasena=hash_password)
            db.session.add(nuevo)
            db.session.commit()
            flash('¡Registro exitoso! Ahora inicia sesión.')
            return redirect(url_for('login'))
    return render_template('usuario/registro.html', error=error)

@app.route('/usuario/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
