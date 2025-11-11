-- SCHEMA SQL - Sistema de Exámenes UNIPAZ
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS unipaz_db;
USE unipaz_db;

-- ==================== TABLAS PRINCIPALES ====================

-- Tabla: Carreras
CREATE TABLE IF NOT EXISTS carreras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    subtitulo VARCHAR(100),
    color VARCHAR(20) DEFAULT '#667eea',
    icono VARCHAR(50) DEFAULT '📚',
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Materias
CREATE TABLE IF NOT EXISTS materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    carrera_id INT NOT NULL,
    semestre INT,
    color VARCHAR(20),
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (carrera_id) REFERENCES carreras(id) ON DELETE CASCADE,
    UNIQUE KEY unique_materia_carrera (nombre, carrera_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(200) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    carrera_id INT,
    nivel INT DEFAULT 1,
    xp INT DEFAULT 0,
    racha_actual INT DEFAULT 0,
    racha_maxima INT DEFAULT 0,
    total_puntos INT DEFAULT 0,
    preguntas_correctas INT DEFAULT 0,
    preguntas_totales INT DEFAULT 0,
    avatar VARCHAR(200) DEFAULT 'default.png',
    rol VARCHAR(20) DEFAULT 'estudiante',
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultima_actividad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (carrera_id) REFERENCES carreras(id) ON DELETE SET NULL,
    INDEX idx_email (email),
    INDEX idx_racha (racha_actual),
    INDEX idx_puntos (total_puntos)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Rankings
CREATE TABLE IF NOT EXISTS rankings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    valor FLOAT NOT NULL,
    posicion INT NOT NULL,
    materia_id INT,
    periodo VARCHAR(20) DEFAULT 'global',
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (materia_id) REFERENCES materias(id) ON DELETE SET NULL,
    UNIQUE KEY unique_ranking (usuario_id, tipo, materia_id, periodo),
    INDEX idx_posicion (posicion),
    INDEX idx_tipo (tipo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Logros (Templates)
CREATE TABLE IF NOT EXISTS logros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    icono VARCHAR(50) DEFAULT '🏆',
    categoria VARCHAR(50),
    requisito_tipo VARCHAR(50),
    requisito_valor INT,
    puntos_reward INT DEFAULT 10,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Usuario Logros (Relación many-to-many)
CREATE TABLE IF NOT EXISTS usuario_logros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    logro_id INT NOT NULL,
    fecha_desbloqueo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (logro_id) REFERENCES logros(id) ON DELETE CASCADE,
    UNIQUE KEY unique_usuario_logro (usuario_id, logro_id),
    INDEX idx_usuario (usuario_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Preguntas
CREATE TABLE IF NOT EXISTS preguntas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto TEXT NOT NULL,
    materia_id INT NOT NULL,
    dificultad VARCHAR(20) DEFAULT 'medio',
    opcion_a VARCHAR(200),
    opcion_b VARCHAR(200),
    opcion_c VARCHAR(200),
    opcion_d VARCHAR(200),
    respuesta_correcta VARCHAR(1),
    explicacion TEXT,
    imagen_url VARCHAR(200),
    creado_por INT,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (materia_id) REFERENCES materias(id) ON DELETE CASCADE,
    FOREIGN KEY (creado_por) REFERENCES usuarios(id) ON DELETE SET NULL,
    INDEX idx_materia (materia_id),
    INDEX idx_dificultad (dificultad)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Respuestas (Registro de respuestas del usuario)
CREATE TABLE IF NOT EXISTS respuestas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    pregunta_id INT NOT NULL,
    respuesta_dada VARCHAR(1),
    es_correcta BOOLEAN,
    tiempo_respuesta INT,
    modo VARCHAR(20),
    materia_id INT,
    fecha_respuesta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(id) ON DELETE CASCADE,
    FOREIGN KEY (materia_id) REFERENCES materias(id) ON DELETE SET NULL,
    INDEX idx_usuario (usuario_id),
    INDEX idx_pregunta (pregunta_id),
    INDEX idx_correcto (es_correcta)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Concursos
CREATE TABLE IF NOT EXISTS concursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    materia_id INT NOT NULL,
    tipo VARCHAR(20) DEFAULT 'eliminacion',
    estado VARCHAR(20) DEFAULT 'activo',
    max_participantes INT DEFAULT 16,
    participantes_actuales INT DEFAULT 0,
    ronda_actual INT DEFAULT 1,
    ganador_id INT,
    segundo_lugar_id INT,
    tercer_lugar_id INT,
    fecha_inicio DATETIME,
    fecha_fin DATETIME,
    tiempo_por_pregunta INT DEFAULT 30,
    premio_1er INT DEFAULT 50,
    premio_2do INT DEFAULT 30,
    premio_3er INT DEFAULT 15,
    creado_por INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (materia_id) REFERENCES materias(id) ON DELETE CASCADE,
    FOREIGN KEY (ganador_id) REFERENCES usuarios(id) ON DELETE SET NULL,
    FOREIGN KEY (segundo_lugar_id) REFERENCES usuarios(id) ON DELETE SET NULL,
    FOREIGN KEY (tercer_lugar_id) REFERENCES usuarios(id) ON DELETE SET NULL,
    FOREIGN KEY (creado_por) REFERENCES usuarios(id) ON DELETE SET NULL,
    INDEX idx_estado (estado),
    INDEX idx_materia (materia_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Participantes Concurso
CREATE TABLE IF NOT EXISTS participantes_concurso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    concurso_id INT NOT NULL,
    usuario_id INT NOT NULL,
    ronda_actual INT DEFAULT 1,
    eliminado BOOLEAN DEFAULT FALSE,
    posicion_final INT,
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_eliminacion DATETIME,
    FOREIGN KEY (concurso_id) REFERENCES concursos(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    UNIQUE KEY unique_participante (concurso_id, usuario_id),
    INDEX idx_concurso (concurso_id),
    INDEX idx_usuario (usuario_id),
    INDEX idx_eliminado (eliminado)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Duelos (Matchups en concursos)
CREATE TABLE IF NOT EXISTS duelos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    concurso_id INT NOT NULL,
    ronda INT NOT NULL,
    usuario1_id INT NOT NULL,
    usuario2_id INT NOT NULL,
    ganador_id INT,
    estado VARCHAR(20) DEFAULT 'pendiente',
    pregunta_id INT,
    fecha_inicio DATETIME,
    fecha_fin DATETIME,
    FOREIGN KEY (concurso_id) REFERENCES concursos(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario1_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario2_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (ganador_id) REFERENCES usuarios(id) ON DELETE SET NULL,
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(id) ON DELETE SET NULL,
    INDEX idx_concurso (concurso_id),
    INDEX idx_ronda (ronda),
    INDEX idx_estado (estado)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Powerups
CREATE TABLE IF NOT EXISTS powerups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    tipo VARCHAR(50),
    icono VARCHAR(50),
    puntos_costo INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Usuario Powerups (Inventario de powerups)
CREATE TABLE IF NOT EXISTS usuario_powerups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    powerup_id INT NOT NULL,
    cantidad INT DEFAULT 0,
    fecha_adquisicion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (powerup_id) REFERENCES powerups(id) ON DELETE CASCADE,
    UNIQUE KEY unique_usuario_powerup (usuario_id, powerup_id),
    INDEX idx_usuario (usuario_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Exámenes (Creados por profesores)
CREATE TABLE IF NOT EXISTS examenes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    materia_id INT NOT NULL,
    creado_por INT NOT NULL,
    descripcion TEXT,
    duracion_minutos INT DEFAULT 30,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (materia_id) REFERENCES materias(id) ON DELETE CASCADE,
    FOREIGN KEY (creado_por) REFERENCES usuarios(id) ON DELETE CASCADE,
    INDEX idx_materia (materia_id),
    INDEX idx_creado_por (creado_por)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Examen Preguntas (Relación many-to-many)
CREATE TABLE IF NOT EXISTS examen_preguntas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    examen_id INT NOT NULL,
    pregunta_id INT NOT NULL,
    orden INT,
    FOREIGN KEY (examen_id) REFERENCES examenes(id) ON DELETE CASCADE,
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(id) ON DELETE CASCADE,
    UNIQUE KEY unique_examen_pregunta (examen_id, pregunta_id),
    INDEX idx_examen (examen_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Examen Powerups
CREATE TABLE IF NOT EXISTS examen_powerups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    examen_id INT NOT NULL,
    powerup_id INT NOT NULL,
    cantidad INT DEFAULT 1,
    cada_n_preguntas INT,
    FOREIGN KEY (examen_id) REFERENCES examenes(id) ON DELETE CASCADE,
    FOREIGN KEY (powerup_id) REFERENCES powerups(id) ON DELETE CASCADE,
    UNIQUE KEY unique_examen_powerup (examen_id, powerup_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ==================== ÍNDICES ADICIONALES ====================

CREATE INDEX idx_usuarios_carrera ON usuarios(carrera_id);
CREATE INDEX idx_usuarios_activo ON usuarios(activo);
CREATE INDEX idx_materias_carrera ON materias(carrera_id);
CREATE INDEX idx_preguntas_creador ON preguntas(creado_por);
CREATE INDEX idx_respuestas_fecha ON respuestas(fecha_respuesta);
CREATE INDEX idx_concursos_creador ON concursos(creado_por);
CREATE INDEX idx_duelos_usuario ON duelos(usuario1_id, usuario2_id);

-- ==================== VISTAS ÚTILES ====================

-- Vista: Top 10 Rachas Global
CREATE OR REPLACE VIEW view_top_10_rachas AS
SELECT 
    @row:=@row+1 AS posicion,
    u.id,
    u.nombre,
    u.avatar,
    c.nombre AS carrera,
    u.racha_actual,
    u.total_puntos
FROM usuarios u
LEFT JOIN carreras c ON u.carrera_id = c.id
CROSS JOIN (SELECT @row:=0) AS t
WHERE u.activo = TRUE
ORDER BY u.racha_actual DESC
LIMIT 10;

-- Vista: Top 10 Porcentaje Éxito Global
CREATE OR REPLACE VIEW view_top_10_porcentaje AS
SELECT 
    @row:=@row+1 AS posicion,
    u.id,
    u.nombre,
    u.avatar,
    c.nombre AS carrera,
    ROUND((u.preguntas_correctas / u.preguntas_totales) * 100, 2) AS porcentaje_exito,
    u.preguntas_correctas,
    u.preguntas_totales
FROM usuarios u
LEFT JOIN carreras c ON u.carrera_id = c.id
CROSS JOIN (SELECT @row:=0) AS t
WHERE u.activo = TRUE AND u.preguntas_totales > 0
ORDER BY (u.preguntas_correctas / u.preguntas_totales) DESC
LIMIT 10;

-- ==================== COLACIONES UTF8 ====================
ALTER DATABASE unipaz_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ==================== LISTO ====================
-- Base de datos creada exitosamente
-- Ahora ejecuta: mysql -u root -p unipaz_db < seeds.sql