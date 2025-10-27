from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash
from models import db, Usuario

usuario = Blueprint('usuario_registro', __name__, template_folder='../templates/usuario')

@usuario.route('/usuario/registro', methods=['GET', 'POST'])
def registro():
    error = ''
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
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
            session['usuarioid'] = nuevo.id
            session['nombre'] = nuevo.nombre
            session['email'] = nuevo.email
            return redirect(url_for('index'))

    return render_template('usuario/registro.html', error=error)
