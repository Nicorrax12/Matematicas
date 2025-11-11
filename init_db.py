#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Inicialización de Base de Datos UNIPAZ
================================================
Este script llena la base de datos con datos de prueba.

Uso:
    python init_db.py

Requiere:
    - Base de datos 'unipaz_db' creada
    - MySQL/MariaDB funcionando
    - Credenciales correctas en la configuración
"""

import mysql.connector
from mysql.connector import Error
import sys

# ========== CONFIGURACIÓN ==========
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Cambiar si tienes contraseña
    'database': 'unipaz_db',
    'charset': 'utf8mb4'
}

# ========== DATOS A INSERTAR ==========

CARRERAS = [
    (1, 'Ingeniería en Sistemas', 'Carrera de Ingeniería', '⚙️', '#667eea'),
    (2, 'Medicina', 'Carrera de Medicina', '🏥', '#ee5a6f'),
    (3, 'Derecho', 'Carrera de Derecho', '⚖️', '#ff9ff3'),
    (4, 'Administración de Empresas', 'Carrera de Administración', '📊', '#1dd1a1'),
]

MATERIAS_POR_CARRERA = {
    1: [  # Ingeniería
        ('Cálculo I', 1, 'Matemáticas básicas'),
        ('Programación I', 1, 'Introducción a programación'),
        ('Álgebra Lineal', 2, 'Matrices y vectores'),
        ('Estructura de Datos', 2, 'Tipos de datos avanzados'),
        ('Base de Datos', 3, 'SQL y BD relacionales'),
        ('Sistemas Operativos', 3, 'Conceptos de SO'),
        ('Redes de Computadores', 4, 'Networking'),
        ('Ingeniería de Software', 4, 'Desarrollo de software'),
    ],
    2: [  # Medicina
        ('Anatomía I', 1, 'Sistema óseo y muscular'),
        ('Biología Celular', 1, 'Células y tejidos'),
        ('Fisiología I', 2, 'Funcionamiento de órganos'),
        ('Bioquímica', 2, 'Procesos químicos'),
        ('Patología', 3, 'Estudio de enfermedades'),
        ('Farmacología', 3, 'Medicamentos'),
        ('Cirugía General', 4, 'Procedimientos quirúrgicos'),
        ('Pediatría', 4, 'Medicina infantil'),
    ],
    3: [  # Derecho
        ('Derecho Constitucional', 1, 'Leyes fundamentales'),
        ('Introducción al Derecho', 1, 'Conceptos básicos'),
        ('Derecho Penal', 2, 'Crímenes y sanciones'),
        ('Derecho Civil', 2, 'Derechos civiles'),
        ('Derecho Laboral', 3, 'Relaciones laborales'),
        ('Derecho Administrativo', 3, 'Administración pública'),
        ('Derecho Mercantil', 4, 'Derecho comercial'),
        ('Derecho Internacional', 4, 'Derecho entre naciones'),
    ],
    4: [  # Administración
        ('Contabilidad Financiera', 1, 'Registros contables'),
        ('Economía General', 1, 'Principios económicos'),
        ('Marketing', 2, 'Estrategias de mercado'),
        ('Administración General', 2, 'Gestión empresarial'),
        ('Recursos Humanos', 3, 'Gestión de personal'),
        ('Finanzas Empresariales', 3, 'Análisis financiero'),
        ('Emprendimiento', 4, 'Crear negocios'),
        ('Gestión Estratégica', 4, 'Planificación estratégica'),
    ],
}

PREGUNTAS_EJEMPLO = [
    {
        'materia_id': 1,
        'texto': '¿Cuál es la derivada de x²?',
        'dificultad': 'facil',
        'opciones': ['x', '2x', '2x²', 'x/2'],
        'respuesta': 'B'
    },
    {
        'materia_id': 1,
        'texto': '¿Cuál es el límite de 1/x cuando x tiende a 0?',
        'dificultad': 'medio',
        'opciones': ['0', '1', 'Infinito', 'No existe'],
        'respuesta': 'C'
    },
    {
        'materia_id': 2,
        'texto': '¿Cuál es la sintaxis correcta en Python?',
        'dificultad': 'facil',
        'opciones': ['print "Hola"', 'print("Hola")', 'PRINT Hola', 'echo Hola'],
        'respuesta': 'B'
    },
]

def conectar_db():
    """Conecta a la base de datos MySQL"""
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        if conexion.is_connected():
            print("✅ Conectado a la base de datos")
            return conexion
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        sys.exit(1)

def crear_tablas(conexion):
    """Crea las tablas si no existen"""
    cursor = conexion.cursor()
    
    # Crear tabla carreras
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carreras (
            id INT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL UNIQUE,
            subtitulo VARCHAR(100),
            icono VARCHAR(50),
            color VARCHAR(20),
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Crear tabla materias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            carrera_id INT NOT NULL,
            semestre INT,
            descripcion TEXT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (carrera_id) REFERENCES carreras(id),
            UNIQUE KEY unique_materia (nombre, carrera_id)
        )
    ''')
    
    # Crear tabla preguntas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS preguntas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            texto TEXT NOT NULL,
            materia_id INT NOT NULL,
            dificultad VARCHAR(20),
            opcion_a VARCHAR(200),
            opcion_b VARCHAR(200),
            opcion_c VARCHAR(200),
            opcion_d VARCHAR(200),
            respuesta_correcta VARCHAR(1),
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (materia_id) REFERENCES materias(id)
        )
    ''')
    
    conexion.commit()
    print("✅ Tablas creadas/verificadas")

def limpiar_datos(conexion):
    """Limpia datos existentes"""
    cursor = conexion.cursor()
    
    try:
        cursor.execute("DELETE FROM preguntas")
        cursor.execute("DELETE FROM materias")
        cursor.execute("DELETE FROM carreras")
        conexion.commit()
        print("✅ Datos anteriores eliminados")
    except Error as e:
        print(f"⚠️  Error al limpiar: {e}")

def insertar_carreras(conexion):
    """Inserta las carreras"""
    cursor = conexion.cursor()
    
    for carrera in CARRERAS:
        try:
            cursor.execute('''
                INSERT INTO carreras (id, nombre, subtitulo, icono, color)
                VALUES (%s, %s, %s, %s, %s)
            ''', carrera)
        except Error as e:
            print(f"⚠️  Carrera duplicada: {carrera[1]}")
    
    conexion.commit()
    print(f"✅ {len(CARRERAS)} carreras insertadas")

def insertar_materias(conexion):
    """Inserta las materias por carrera"""
    cursor = conexion.cursor()
    total = 0
    
    for carrera_id, materias in MATERIAS_POR_CARRERA.items():
        semestre = 1
        for nombre, sem, descripcion in materias:
            try:
                cursor.execute('''
                    INSERT INTO materias (nombre, carrera_id, semestre, descripcion)
                    VALUES (%s, %s, %s, %s)
                ''', (nombre, carrera_id, sem, descripcion))
                total += 1
            except Error as e:
                print(f"⚠️  Error insertando {nombre}: {e}")
    
    conexion.commit()
    print(f"✅ {total} materias insertadas")

def insertar_preguntas(conexion):
    """Inserta preguntas de ejemplo"""
    cursor = conexion.cursor()
    
    for i, pregunta in enumerate(PREGUNTAS_EJEMPLO):
        try:
            respuesta_map = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}
            respuesta = respuesta_map[pregunta['respuesta']]
            
            cursor.execute('''
                INSERT INTO preguntas 
                (texto, materia_id, dificultad, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                pregunta['texto'],
                pregunta['materia_id'],
                pregunta['dificultad'],
                pregunta['opciones'][0],
                pregunta['opciones'][1],
                pregunta['opciones'][2],
                pregunta['opciones'][3],
                respuesta
            ))
        except Error as e:
            print(f"❌ Error con pregunta {i+1}: {e}")
    
    conexion.commit()
    print(f"✅ {len(PREGUNTAS_EJEMPLO)} preguntas insertadas")

def verificar_datos(conexion):
    """Verifica que los datos se insertaron correctamente"""
    cursor = conexion.cursor()
    
    # Contar carreras
    cursor.execute("SELECT COUNT(*) FROM carreras")
    num_carreras = cursor.fetchone()[0]
    
    # Contar materias
    cursor.execute("SELECT COUNT(*) FROM materias")
    num_materias = cursor.fetchone()[0]
    
    # Contar preguntas
    cursor.execute("SELECT COUNT(*) FROM preguntas")
    num_preguntas = cursor.fetchone()[0]
    
    print("\n" + "="*50)
    print("📊 RESUMEN DE DATOS INSERTADOS")
    print("="*50)
    print(f"📚 Carreras: {num_carreras}")
    print(f"📖 Materias: {num_materias}")
    print(f"❓ Preguntas: {num_preguntas}")
    print("="*50)

def main():
    """Función principal"""
    print("\n" + "="*50)
    print("🗄️  INICIALIZADOR DE BD - UNIPAZ QUIZ SYSTEM")
    print("="*50 + "\n")
    
    conexion = conectar_db()
    
    try:
        crear_tablas(conexion)
        limpiar_datos(conexion)
        insertar_carreras(conexion)
        insertar_materias(conexion)
        insertar_preguntas(conexion)
        verificar_datos(conexion)
        
        print("\n✅ ¡Base de datos inicializada exitosamente!\n")
        
    except Error as e:
        print(f"❌ Error: {e}")
    finally:
        if conexion.is_connected():
            conexion.close()

if __name__ == '__main__':
    main()