from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from models import db, Usuario

usuario = Blueprint('usuario', __name__, template_folder='../templates/usuario')

@usuario.route('/usuario/login', methods=['GET', 'POST'])
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
