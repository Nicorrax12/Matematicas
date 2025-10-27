from conexion import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    rachaactual = db.Column(db.Integer, default=0)      # preguntas seguidas correctas actuales
    mejorracha = db.Column(db.Integer, default=0)       # mejor racha histórica
    preguntas_acertadas = db.Column(db.Integer, default=0)
    preguntas_total = db.Column(db.Integer, default=0)

class Examen(db.Model):
    __tablename__ = 'examenes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(10), unique=True, nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    creador_id = db.Column(db.Integer, nullable=True)
    contrasena = db.Column(db.String(128), nullable=False)
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.now())
    preguntas = db.relationship('PreguntaExamen', backref='examen', lazy=True)

class Nivel(db.Model):
    __tablename__ = 'niveles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80), nullable=False)

class PreguntaExamen(db.Model):
    __tablename__ = 'preguntas_examen'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    examen_id = db.Column(db.Integer, db.ForeignKey('examenes.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    opcion_a = db.Column(db.String(255), nullable=False)
    opcion_b = db.Column(db.String(255), nullable=False)
    opcion_c = db.Column(db.String(255), nullable=False)
    opcion_d = db.Column(db.String(255), nullable=False)
    correcta = db.Column(db.String(1), nullable=False)


class ConcursoRonda(db.Model):
    __tablename__ = 'concursorondas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    examenid = db.Column(db.Integer, db.ForeignKey('examenes.id', ondelete='CASCADE'))
    rondanumero = db.Column(db.Integer)
    preguntaactualid = db.Column(db.Integer)
    tiemporonda = db.Column(db.Integer)

class Pregunta(db.Model):
    __tablename__ = 'preguntas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.Text, nullable=False)
    opcion_a = db.Column(db.String(255), nullable=False)
    opcion_b = db.Column(db.String(255), nullable=False)
    opcion_c = db.Column(db.String(255), nullable=False)
    opcion_d = db.Column(db.String(255), nullable=False)
    correcta = db.Column(db.String(1), nullable=False)   # 'a', 'b', 'c' o 'd'
    nivel = db.Column(db.Integer, nullable=False)         # del 1 al 12

class ResultadoExamen(db.Model):
    __tablename__ = 'resultados_examen'
    id = db.Column(db.Integer, primary_key=True)
    examen_id = db.Column(db.Integer, db.ForeignKey('examenes.id'), nullable=False)
    usuario = db.Column(db.String(80), nullable=False)  # o usuario_id si tienes login
    puntaje = db.Column(db.Integer)
    total = db.Column(db.Integer)
    tiempo = db.Column(db.Integer)  # en segundos
    fecha_inicio = db.Column(db.DateTime)
    fecha_fin = db.Column(db.DateTime)
