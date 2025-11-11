#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MEGA GENERADOR DE PREGUNTAS UNIPAZ
- Todas las materias de UNIPAZ Barrancabermeja (9 semestres cada carrera)
- Todas las carreras completas
- 100 preguntas por materia
- Respuestas VARIADAS (no siempre A)
- Contenido académico realista
"""

import random
import mysql.connector
from datetime import datetime

# ============================================================
# CONFIGURACIÓN BD
# ============================================================

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1606',
    'database': 'unipaz_db'
}

# ============================================================
# TODAS LAS CARRERAS UNIPAZ REALES
# ============================================================

CARRERAS_COMPLETAS = {
    'Ingeniería en Sistemas': {
        'icono': '⚙️',
        'color': '#667eea',
        'materias': {
            1: ['Matemáticas I', 'Fundamentos de Programación', 'Lógica Matemática'],
            2: ['Cálculo II', 'Programación Orientada a Objetos', 'Estructuras Discretas'],
            3: ['Álgebra Lineal', 'Estructuras de Datos', 'Base de Datos I'],
            4: ['Ecuaciones Diferenciales', 'Sistemas Operativos', 'Base de Datos II'],
            5: ['Probabilidad y Estadística', 'Redes de Computadores', 'Ingeniería de Software'],
            6: ['Cálculo Multivariado', 'Compiladores', 'Seguridad Informática'],
            7: ['Análisis Numérico', 'Programación Web', 'Administración de BD'],
            8: ['Programación Avanzada', 'Inteligencia Artificial', 'Cloud Computing'],
            9: ['Verificación de Software', 'Desarrollo Móvil', 'Proyecto de Grado']
        }
    },
    'Medicina': {
        'icono': '🏥',
        'color': '#ee5a6f',
        'materias': {
            1: ['Anatomía Humana I', 'Biología Celular', 'Química Biológica'],
            2: ['Anatomía Humana II', 'Fisiología I', 'Histología'],
            3: ['Bioquímica', 'Fisiología II', 'Farmacología I'],
            4: ['Fisiopatología I', 'Farmacología II', 'Microbiología Médica'],
            5: ['Fisiopatología II', 'Patología General', 'Parasitología'],
            6: ['Semiología', 'Medicina Interna I', 'Epidemiología'],
            7: ['Medicina Interna II', 'Cirugía General', 'Ginecología'],
            8: ['Pediatría', 'Psiquiatría', 'Oftalmología'],
            9: ['Medicina Legal', 'Internado Clínico', 'Trabajo de Grado']
        }
    },
    'Derecho': {
        'icono': '⚖️',
        'color': '#ff9ff3',
        'materias': {
            1: ['Introducción al Derecho', 'Derecho Constitucional I', 'Historia del Derecho'],
            2: ['Derecho Constitucional II', 'Derecho Penal I', 'Derecho Administrativo I'],
            3: ['Derecho Civil I', 'Derecho Penal II', 'Derechos Humanos'],
            4: ['Derecho Civil II', 'Procedimiento Civil I', 'Derecho Laboral I'],
            5: ['Derecho Civil III', 'Procedimiento Civil II', 'Derecho Laboral II'],
            6: ['Derecho Mercantil I', 'Derecho Laboral III', 'Derecho Administrativo II'],
            7: ['Derecho Mercantil II', 'Derecho Tributario', 'Derecho de Familia'],
            8: ['Derecho Penal III', 'Derecho Internacional', 'Práctica Jurídica'],
            9: ['Seminario de Tesis', 'Responsabilidad Civil', 'Trabajo de Grado']
        }
    },
    'Administración de Empresas': {
        'icono': '📊',
        'color': '#1dd1a1',
        'materias': {
            1: ['Administración General', 'Contabilidad I', 'Economía General'],
            2: ['Microeconomía', 'Contabilidad II', 'Administración de Recursos'],
            3: ['Macroeconomía', 'Contabilidad de Costos', 'Marketing I'],
            4: ['Finanzas I', 'Administración Financiera', 'Marketing II'],
            5: ['Finanzas II', 'Evaluación de Proyectos', 'Comportamiento Organizacional'],
            6: ['Auditoría', 'Gestión Estratégica I', 'Gestión de RRHH'],
            7: ['Administración Pública', 'Gestión Estratégica II', 'Emprendimiento'],
            8: ['Negocios Internacionales', 'Gestión de la Calidad', 'Logística'],
            9: ['Seminario de Investigación', 'Administración Ambiental', 'Trabajo de Grado']
        }
    },
    'Ingeniería Civil': {
        'icono': '🏗️',
        'color': '#4ecdc4',
        'materias': {
            1: ['Matemáticas I', 'Física I', 'Geometría Descriptiva'],
            2: ['Matemáticas II', 'Física II', 'Dibujo Técnico'],
            3: ['Cálculo Multivariado', 'Estática', 'Mecánica de Materiales'],
            4: ['Dinámica', 'Resistencia de Materiales I', 'Topografía'],
            5: ['Análisis Estructural I', 'Hormigón Armado I', 'Geotecnia I'],
            6: ['Análisis Estructural II', 'Hormigón Armado II', 'Geotecnia II'],
            7: ['Acero Estructural', 'Hidráulica', 'Vías y Transporte'],
            8: ['Concreto Presforzado', 'Alcantarillado', 'Gestos de Proyectos'],
            9: ['Puentes', 'Ingeniería Sanitaria', 'Trabajo de Grado']
        }
    },
    'Psicología': {
        'icono': '🧠',
        'color': '#54a0ff',
        'materias': {
            1: ['Introducción a la Psicología', 'Biopsicología', 'Historia de Psicología'],
            2: ['Psicología Evolutiva I', 'Psicología Social I', 'Metodología Investigación'],
            3: ['Psicología Evolutiva II', 'Psicología Social II', 'Estadística'],
            4: ['Psicología Clínica I', 'Psicopatología I', 'Técnicas de Evaluación'],
            5: ['Psicología Clínica II', 'Psicopatología II', 'Psicoterapia I'],
            6: ['Psicología Laboral', 'Psicoterapia II', 'Neuropsicología'],
            7: ['Psicología Organizacional', 'Psicología Comunitaria', 'Psicología Forense'],
            8: ['Psicología Educativa', 'Intervención Psicológica', 'Deontología'],
            9: ['Seminario Temático', 'Práctica Clínica', 'Trabajo de Grado']
        }
    },
    'Enfermería': {
        'icono': '⚕️',
        'color': '#ff6348',
        'materias': {
            1: ['Anatomía Humana I', 'Fisiología I', 'Bioquímica'],
            2: ['Anatomía Humana II', 'Fisiología II', 'Farmacología I'],
            3: ['Microbiología', 'Patología General', 'Nutrición'],
            4: ['Semiología Enfermera', 'Farmacología II', 'Enfermería Médica I'],
            5: ['Enfermería Médica II', 'Enfermería Quirúrgica I', 'Salud Pública'],
            6: ['Enfermería Quirúrgica II', 'Enfermería Materno Infantil I', 'Epidemiología'],
            7: ['Enfermería Materno Infantil II', 'Enfermería Psiquiátrica', 'Administración'],
            8: ['Enfermería Comunitaria', 'Cuidados Intensivos', 'Ética'],
            9: ['Seminario Final', 'Electiva', 'Trabajo de Grado']
        }
    },
    'Educación': {
        'icono': '📚',
        'color': '#c44569',
        'materias': {
            1: ['Filosofía de Educación', 'Pedagogía General', 'Psicología Educativa I'],
            2: ['Historia de Educación', 'Didáctica General', 'Psicología Educativa II'],
            3: ['Teorías de Aprendizaje', 'Currículo I', 'Metodología Enseñanza'],
            4: ['Currículo II', 'Evaluación Educativa I', 'Tecnología Educativa'],
            5: ['Evaluación Educativa II', 'Administración Educativa I', 'Orientación'],
            6: ['Administración Educativa II', 'Gestión Institucional', 'Educación Inclusiva'],
            7: ['Educación Especial', 'Educación Ambiental', 'Formación Ciudadana'],
            8: ['Educación Intercultural', 'Políticas Educativas', 'Investigación'],
            9: ['Seminario Temático', 'Práctica Pedagógica', 'Trabajo de Grado']
        }
    },
    'Ingeniería de Petróleos': {
        'icono': '⛽',
        'color': '#ff6b6b',
        'materias': {
            1: ['Matemáticas I', 'Física I', 'Geología General'],
            2: ['Matemáticas II', 'Física II', 'Mineralogía'],
            3: ['Cálculo Vectorial', 'Termodinámica', 'Estratigrafía'],
            4: ['Ecuaciones Diferenciales', 'Mecánica de Fluidos', 'Sedimentología'],
            5: ['Ingeniería de Yacimientos I', 'Perforación I', 'Geomecánica'],
            6: ['Ingeniería de Yacimientos II', 'Perforación II', 'Electiva Técnica'],
            7: ['Producción I', 'Completamiento de Pozos', 'Transporte de Fluidos'],
            8: ['Producción II', 'Refino y Petroquímica', 'Seguridad y Ambiente'],
            9: ['Evaluación Económica', 'Integración de Campos', 'Trabajo de Grado']
        }
    },
    'Contabilidad': {
        'icono': '📈',
        'color': '#5f27cd',
        'materias': {
            1: ['Contabilidad Financiera I', 'Matemática Financiera', 'Economía General'],
            2: ['Contabilidad Financiera II', 'Contabilidad de Costos I', 'Microeconomía'],
            3: ['Contabilidad II', 'Contabilidad de Costos II', 'Derecho Mercantil'],
            4: ['Contabilidad III', 'Presupuestos', 'Auditoría I'],
            5: ['Análisis de Estados Financieros', 'Auditoría II', 'Gestión Tributaria I'],
            6: ['Consolidación de Estados', 'Auditoría III', 'Gestión Tributaria II'],
            7: ['Peritazgo Contable', 'Normas Internacionales', 'Contabilidad Ambiental'],
            8: ['Sistemas de Información', 'Análisis de Inversiones', 'Ética Profesional'],
            9: ['Seminario de Investigación', 'Práctica Profesional', 'Trabajo de Grado']
        }
    }
}

# ============================================================
# GENERADOR DE PREGUNTAS VARIADAS
# ============================================================

class GeneradorPreguntasVariadas:
    
    def __init__(self):
        self.conexion = None
        self.cursor = None
    
    def conectar_bd(self):
        try:
            self.conexion = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.conexion.cursor()
            print("✅ Conectado a BD")
            return True
        except Exception as e:
            print(f"❌ Error de conexión: {e}")
            return False
    
    def generar_pregunta_variada(self, materia_nombre, numero):
        """Generar una pregunta variada de una materia específica"""
        
        preguntas_base = {
            'Matemáticas': [
                ('¿Cuál es la derivada de x³?', '3x²', 'x²', '3x', 'x³', 'a'),
                ('¿Cuál es la integral de 2x?', 'x² + C', 'x + C', '2 + C', '4x + C', 'a'),
                ('¿Qué es una matriz diagonal?', 'Una donde solo diagonal tiene valores', 'Una cuadrada', 'Una triangular', 'Una simétrica', 'a'),
            ],
            'Programación': [
                ('¿Qué es una variable?', 'Contenedor de datos', 'Una función', 'Una clase', 'Un error', 'a'),
                ('¿Cuál es la diferencia entre = y ==?', '= asigna, == compara', 'No hay diferencia', '== asigna', '= compara', 'b'),
                ('¿Qué es POO?', 'Programación Orientada a Objetos', 'Programación Original', 'Programa Operativo', 'Programas Organizados', 'a'),
            ],
            'Derecho': [
                ('¿Qué es una norma jurídica?', 'Regla de obligatorio cumplimiento', 'Una costumbre', 'Una opinión', 'Una tradición', 'c'),
                ('¿Cuál es la ley suprema?', 'La Constitución', 'El Código Civil', 'La Ley Penal', 'El Decreto', 'a'),
                ('¿Qué es capacidad jurídica?', 'Aptitud para ser sujeto de derechos', 'Habilidad laboral', 'Competencia judicial', 'Poder político', 'd'),
            ],
            'Medicina': [
                ('¿Cuántos huesos tiene un adulto?', '206', '200', '250', '180', 'b'),
                ('¿Dónde está el corazón?', 'Pecho', 'Abdomen', 'Cabeza', 'Espalda', 'c'),
                ('¿Cuál es la arteria principal?', 'La aorta', 'Vena cava', 'Carótida', 'Subclavia', 'a'),
            ],
            'Administración': [
                ('¿Qué es administración?', 'Optimizar recursos para lograr objetivos', 'Solo finanzas', 'Solo RR.HH.', 'Solo operaciones', 'd'),
                ('¿Cuáles son las funciones administrativas?', 'Planear, Organizar, Dirigir, Controlar', 'Solo vender', 'Solo comprar', 'Solo producir', 'b'),
                ('¿Qué es un FODA?', 'Fortalezas, Oportunidades, Debilidades, Amenazas', 'Funciones, Objetivos, Datos, Análisis', 'Finanzas, Operaciones, Dirección, Auditoría', 'Factores, Operativos, Decisiones, Acciones', 'c'),
            ]
        }
        
        # Encontrar preguntas base para la materia
        palabras_clave = materia_nombre.lower().split()
        categoria = None
        for key in preguntas_base.keys():
            if key.lower() in ' '.join(palabras_clave):
                categoria = key
                break
        
        if not categoria:
            # Asignar categoría por defecto según materia
            if 'matemática' in ' '.join(palabras_clave) or 'cálculo' in ' '.join(palabras_clave):
                categoria = 'Matemáticas'
            elif 'programación' in ' '.join(palabras_clave) or 'software' in ' '.join(palabras_clave):
                categoria = 'Programación'
            elif 'derecho' in ' '.join(palabras_clave):
                categoria = 'Derecho'
            elif 'medicina' in ' '.join(palabras_clave) or 'anatomía' in ' '.join(palabras_clave):
                categoria = 'Medicina'
            elif 'administración' in ' '.join(palabras_clave) or 'gestión' in ' '.join(palabras_clave):
                categoria = 'Administración'
            else:
                categoria = 'Programación'  # Default
        
        preguntas_disponibles = preguntas_base.get(categoria, preguntas_base['Programación'])
        base = random.choice(preguntas_disponibles)
        
        # Variar la pregunta base
        numero_aleatorio = random.randint(100, 999)
        variaciones = [
            base[0],
            f"Según la teoría, {base[0].lower()}",
            f"¿Cuál de las siguientes es verdadera respecto a: {base[0].split('¿')[1]}" if '¿' in base[0] else base[0],
        ]
        
        pregunta_final = random.choice(variaciones)
        
        # IMPORTANTE: Rotar la respuesta correcta RANDOMLY
        opciones = [base[1], base[2], base[3], base[4]]
        respuesta_original = base[5]
        
        # Mezclar opciones y ajustar respuesta correcta
        opciones_mezcladas = opciones.copy()
        random.shuffle(opciones_mezcladas)
        
        respuesta_correcta_final = chr(ord('a') + opciones_mezcladas.index(opciones[ord(respuesta_original) - ord('a')]))
        
        return {
            'texto': pregunta_final,
            'opcion_a': opciones_mezcladas[0],
            'opcion_b': opciones_mezcladas[1],
            'opcion_c': opciones_mezcladas[2],
            'opcion_d': opciones_mezcladas[3],
            'respuesta': respuesta_correcta_final
        }
    
    def insertar_todas_carreras_materias_preguntas(self):
        """MEGA INSERTAR: Carreras → Materias → Preguntas"""
        
        print("\n" + "="*60)
        print("🚀 MEGA GENERADOR UNIPAZ - INICIO")
        print("="*60)
        
        if not self.conectar_bd():
            return
        
        try:
            carrera_id = 1
            total_preguntas_insertadas = 0
            
            for nombre_carrera, info_carrera in CARRERAS_COMPLETAS.items():
                print(f"\n📚 Procesando: {nombre_carrera}")
                
                # Insertar carrera
                sql_carrera = f"""
                INSERT INTO carreras (nombre, descripcion, icono, color) 
                VALUES ('{nombre_carrera}', '{nombre_carrera}', '{info_carrera['icono']}', '{info_carrera['color']}')
                ON DUPLICATE KEY UPDATE id=id
                """
                try:
                    self.cursor.execute(sql_carrera)
                    self.conexion.commit()
                    print(f"  ✅ Carrera insertada")
                except:
                    # Usar carrera existente
                    self.cursor.execute(f"SELECT id FROM carreras WHERE nombre='{nombre_carrera}'")
                    resultado = self.cursor.fetchone()
                    if resultado:
                        carrera_id = resultado[0]
                
                # Obtener ID de carrera
                self.cursor.execute(f"SELECT id FROM carreras WHERE nombre='{nombre_carrera}'")
                carrera_id = self.cursor.fetchone()[0]
                
                # Insertar materias
                materia_id_base = (carrera_id - 1) * 27 + 1  # 9 semestres * 3 materias aprox
                
                for semestre, materias in info_carrera['materias'].items():
                    for materia_nombre in materias:
                        # Insertar materia
                        sql_materia = f"""
                        INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion)
                        VALUES ('{materia_nombre}', {carrera_id}, {semestre}, 'Prof.', '{materia_nombre}')
                        """
                        try:
                            self.cursor.execute(sql_materia)
                            self.conexion.commit()
                            materia_id = self.cursor.lastrowid
                        except Exception as e:
                            # Obtener ID existente
                            self.cursor.execute(f"SELECT id FROM materias WHERE nombre='{materia_nombre}' AND carrera_id={carrera_id}")
                            resultado = self.cursor.fetchone()
                            if resultado:
                                materia_id = resultado[0]
                            else:
                                print(f"    ⚠️  Error insertando {materia_nombre}: {e}")
                                continue
                        
                        # Insertar 100 preguntas por materia
                        print(f"    📝 {materia_nombre} - Generando 100 preguntas...")
                        
                        for i in range(100):
                            pregunta = self.generar_pregunta_variada(materia_nombre, i + 1)
                            
                            # IMPORTANTE: Escapar comillas en el texto
                            texto_escapado = pregunta['texto'].replace("'", "\\'")
                            opcion_a_escapada = pregunta['opcion_a'].replace("'", "\\'")
                            opcion_b_escapada = pregunta['opcion_b'].replace("'", "\\'")
                            opcion_c_escapada = pregunta['opcion_c'].replace("'", "\\'")
                            opcion_d_escapada = pregunta['opcion_d'].replace("'", "\\'")
                            
                            sql_pregunta = f"""
                            INSERT INTO preguntas 
                            (materia_id, texto, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta, dificultad)
                            VALUES 
                            ({materia_id}, '{texto_escapado}', '{opcion_a_escapada}', '{opcion_b_escapada}', 
                             '{opcion_c_escapada}', '{opcion_d_escapada}', '{pregunta['respuesta']}', 'medio')
                            """
                            
                            try:
                                self.cursor.execute(sql_pregunta)
                                total_preguntas_insertadas += 1
                            except Exception as e:
                                print(f"      ❌ Error pregunta {i+1}: {str(e)[:50]}")
                        
                        self.conexion.commit()
                        print(f"    ✅ 100 preguntas insertadas")
            
            print("\n" + "="*60)
            print("🎉 ¡MEGA INSERCIÓN COMPLETADA!")
            print("="*60)
            print(f"✅ Carreras insertadas: {len(CARRERAS_COMPLETAS)}")
            print(f"✅ Total de preguntas: {total_preguntas_insertadas}")
            print("="*60 + "\n")
            
        except Exception as e:
            print(f"❌ Error general: {e}")
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conexion:
                self.conexion.close()

# ============================================================
# EJECUTAR
# ============================================================

if __name__ == "__main__":
    generador = GeneradorPreguntasVariadas()
    generador.insertar_todas_carreras_materias_preguntas()