-- ============================================================
-- SEED DATA PARA UNIPAZ QUIZ SYSTEM
-- Inserta datos de prueba para que funcione el flujo completo
-- ============================================================

USE unipaz_db;

-- ============================================================
-- 1. INSERTAR MATERIAS POR CARRERA
-- ============================================================

-- Ingeniería (carrera_id = 1)
INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion) VALUES
('Cálculo I', 1, 1, 'Dr. García', 'Fundamentos de cálculo diferencial'),
('Programación I', 1, 1, 'Ing. López', 'Introducción a la programación'),
('Álgebra Lineal', 1, 2, 'Dr. Martínez', 'Matrices y espacios vectoriales'),
('Estructura de Datos', 1, 2, 'Ing. Rodríguez', 'Listas, árboles y grafos'),
('Base de Datos', 1, 3, 'Ing. Pérez', 'SQL y diseño de BD');

-- Medicina (carrera_id = 2)
INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion) VALUES
('Anatomía I', 2, 1, 'Dr. Cortés', 'Sistema óseo y muscular'),
('Fisiología', 2, 2, 'Dra. Rivera', 'Funcionamiento de órganos'),
('Patología', 2, 3, 'Dr. Morales', 'Estudio de enfermedades'),
('Farmacología', 2, 4, 'Dra. Sánchez', 'Medicamentos y sus efectos'),
('Cirugía General', 2, 5, 'Dr. Jiménez', 'Procedimientos quirúrgicos');

-- Derecho (carrera_id = 3)
INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion) VALUES
('Derecho Constitucional', 3, 1, 'Dr. Ávila', 'Leyes fundamentales'),
('Derecho Penal', 3, 2, 'Dra. Gómez', 'Crímenes y sanciones'),
('Derecho Civil', 3, 3, 'Dr. Castillo', 'Derechos y obligaciones civiles'),
('Derecho Laboral', 3, 4, 'Dra. Torres', 'Relaciones laborales'),
('Derecho Administrativo', 3, 5, 'Dr. Vargas', 'Administración pública');

-- Administración (carrera_id = 4)
INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion) VALUES
('Contabilidad Financiera', 4, 1, 'CPA López', 'Registros contables'),
('Marketing', 4, 2, 'Lic. Mendez', 'Estrategias de mercado'),
('Recursos Humanos', 4, 3, 'Dra. Silva', 'Gestión de personal'),
('Finanzas Empresariales', 4, 4, 'MBA García', 'Análisis financiero'),
('Emprendimiento', 4, 5, 'Ing. Ruiz', 'Crear tu propio negocio');

-- ============================================================
-- 2. INSERTAR PREGUNTAS DE PRUEBA (INGENIERÍA - CÁLCULO)
-- ============================================================

-- Matemáticas I - Carrera 1 (Ingeniería)
INSERT INTO preguntas (materia_id, texto, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta, dificultad, explicacion) VALUES
(1, '¿Cuál es la derivada de f(x) = 2x³ + 5x - 3?', '6x² + 5', '6x² - 5', '2x² + 5', 'x² + 5', 'a', 'medio', 'La derivada de 2x³ es 6x², y la de 5x es 5'),
(1, '¿Cuál es el límite cuando x tiende a 2 de (x² - 4)/(x - 2)?', '0', '2', '4', '8', 'c', 'medio', 'Factorizar: (x-2)(x+2)/(x-2) = x+2 = 4'),
(1, '¿Cuál es la integral de ∫(3x² + 2x)dx?', 'x³ + x² + C', 'x³ + x + C', '3x³ + 2x + C', '6x + 2 + C', 'a', 'medio', 'La integral de 3x² es x³, la de 2x es x²'),
(1, '¿En qué punto se encuentra el máximo local de f(x) = x² - 4x + 3?', 'x = 0', 'x = 2', 'x = 1', 'x = 3', 'b', 'dificil', 'f\'(x) = 2x - 4 = 0, entonces x = 2'),
(1, '¿Cuál es la continuidad de f(x) = 1/x en x = 0?', 'Continua', 'Discontinua de salto', 'Discontinua infinita', 'Continua por partes', 'c', 'dificil', 'En x=0 hay una discontinuidad infinita'),
(1, '¿Cuál es la serie de Taylor de sin(x) alrededor de x = 0?', 'x - x³/3! + x⁵/5! - ...', 'x + x³/3! + x⁵/5! + ...', '1 - x²/2! + x⁴/4! - ...', 'x²/2! + x⁴/4! + ...', 'a', 'dificil', 'Alternancia de signos y factoriales impares'),
(1, '¿Cuál es la derivada de f(x) = e^x?', 'e^x', 'x·e^x', '1', 'e^(x-1)', 'a', 'facil', 'La derivada de e^x es e^x'),
(1, '¿Cuál es el área bajo la curva y = x² de 0 a 2?', '8/3', '4', '16', '2', 'a', 'medio', '∫(0 a 2) x² dx = [x³/3] = 8/3'),
(1, '¿Cuál es el límite de sin(x)/x cuando x → 0?', '0', '1', '∞', '-1', 'b', 'medio', 'Este es un límite notable igual a 1'),
(1, '¿Cuál es la second derivada de f(x) = 3x⁴ - 2x²?', '36x² - 4', '12x³ - 4x', '36x² + 4', '12x³ + 4x', 'a', 'medio', 'f\'(x) = 12x³ - 4x, f\'\'(x) = 36x² - 4');

-- Programación I - Carrera 1 (Ingeniería)
INSERT INTO preguntas (materia_id, texto, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta, dificultad, explicacion) VALUES
(2, '¿Cuál es el tipo de dato para un número entero en Python?', 'str', 'int', 'float', 'bool', 'b', 'facil', 'int representa números enteros'),
(2, '¿Qué resultado da print(5 // 2)?', '2.5', '2', '3', '2.0', 'b', 'facil', '// es división entera'),
(2, '¿Cuál es la forma correcta de definir una función en Python?', 'function miFuncion():', 'def miFuncion():', 'func miFuncion():', 'function: miFuncion', 'b', 'facil', 'def es la palabra clave para funciones'),
(2, '¿Qué es un bucle for?', 'Una estructura condicional', 'Una forma de repetir código', 'Una función', 'Una librería', 'b', 'facil', 'for permite iterar múltiples veces'),
(2, '¿Cuál es la salida de range(5)?', '[0,1,2,3,4]', '(0,1,2,3,4)', '[1,2,3,4,5]', '[0,1,2,3,4,5]', 'a', 'medio', 'range comienza desde 0');

-- ============================================================
-- 3. INSERTAR USUARIOS DE PRUEBA
-- ============================================================

INSERT INTO usuarios (nombre, email, password_hash, carrera_id, racha_actual, racha_maxima, total_puntos, preguntas_correctas, preguntas_totales, rol, activo) VALUES
('Juan Carlos Pérez', 'juan.carlos@unipaz.edu', '$2b$12$hashedpassword123', 1, 127, 200, 2450, 450, 460, 'estudiante', 1),
('María González López', 'maria.gonzalez@unipaz.edu', '$2b$12$hashedpassword456', 2, 85, 150, 1800, 380, 400, 'estudiante', 1),
('Carlos Rodríguez Silva', 'carlos.rodriguez@unipaz.edu', '$2b$12$hashedpassword789', 3, 62, 120, 1200, 250, 350, 'estudiante', 1),
('Ana Martínez Torres', 'ana.martinez@unipaz.edu', '$2b$12$hashedpassword012', 4, 95, 180, 2100, 420, 450, 'estudiante', 1),
('Pedro García Jiménez', 'pedro.garcia@unipaz.edu', '$2b$12$hashedpassword345', 1, 45, 100, 850, 170, 250, 'profesor', 1),
('Laura Fernández Díaz', 'laura.fernandez@unipaz.edu', '$2b$12$hashedpassword678', 2, 15, 50, 300, 50, 100, 'estudiante', 1),
('Admin UNIPAZ', 'admin@unipaz.edu', '$2b$12$adminpassword', 1, 0, 0, 0, 0, 0, 'admin', 1);

-- ============================================================
-- 4. INSERTAR RESPUESTAS DE PRUEBA
-- ============================================================

INSERT INTO respuestas (usuario_id, pregunta_id, respuesta_dada, es_correcta, tiempo_respuesta, modo, materia_id) VALUES
(1, 1, 'a', 1, 25, 'normal', 1),
(1, 2, 'c', 1, 30, 'normal', 1),
(1, 3, 'a', 1, 20, 'normal', 1),
(1, 4, 'b', 1, 45, 'hardcore', 1),
(1, 5, 'c', 0, 60, 'hardcore', 1),
(2, 1, 'a', 1, 20, 'normal', 1),
(2, 2, 'b', 1, 25, 'normal', 1),
(3, 1, 'b', 0, 15, 'pesadilla', 1),
(4, 1, 'a', 1, 10, 'normal', 1),
(4, 2, 'c', 1, 35, 'normal', 1);

-- ============================================================
-- 5. INSERTAR LOGROS DESBLOQUEADOS
-- ============================================================

INSERT INTO logros_desbloqueados (usuario_id, logro_id, fecha_desbloqueado) VALUES
(1, 1, '2025-11-01 10:00:00'),
(1, 2, '2025-11-02 14:30:00'),
(1, 3, '2025-11-05 09:15:00'),
(2, 1, '2025-11-01 11:00:00'),
(2, 2, '2025-11-03 16:20:00'),
(4, 1, '2025-11-02 08:00:00'),
(4, 2, '2025-11-04 12:45:00'),
(4, 5, '2025-11-06 15:00:00');

-- ============================================================
-- ✅ DATOS INSERTADOS EXITOSAMENTE
-- ============================================================

-- Verifica que todo se insertó:
SELECT COUNT(*) as 'Total Materias' FROM materias;
SELECT COUNT(*) as 'Total Preguntas' FROM preguntas;
SELECT COUNT(*) as 'Total Usuarios' FROM usuarios;
SELECT COUNT(*) as 'Total Respuestas' FROM respuestas;
SELECT COUNT(*) as 'Total Logros Desbloqueados' FROM logros_desbloqueados;

-- Ver usuarios
SELECT id, nombre, email, carrera_id, total_puntos, racha_actual FROM usuarios;

-- Ver materias por carrera
SELECT m.id, m.nombre, c.nombre as carrera FROM materias m 
JOIN carreras c ON m.carrera_id = c.id 
ORDER BY c.id;