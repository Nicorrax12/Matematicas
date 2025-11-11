// localStorage-helper.js - Gestor de localStorage UNIPAZ

console.log('✅ localStorage-helper.js cargado');

const STORAGE_KEYS = {
    // Autenticación
    TOKEN: 'unipaz_token',
    USUARIO: 'unipaz_usuario',
    
    // Preferencias
    TEMA: 'unipaz_tema',
    IDIOMA: 'unipaz_idioma',
    NOTIFICACIONES: 'unipaz_notificaciones',
    
    // Datos temporales
    MATERIA_SELECCIONADA: 'unipaz_materia',
    QUIZ_EN_PROGRESO: 'unipaz_quiz_progreso',
    ULTIMO_DUELO: 'unipaz_ultimo_duelo',
    
    // Caché
    CARRERAS_CACHE: 'unipaz_carreras_cache',
    MATERIAS_CACHE: 'unipaz_materias_cache',
    RANKINGS_CACHE: 'unipaz_rankings_cache'
};

/**
 * Guardar dato en localStorage
 */
function guardarDato(clave, valor, tipo = 'json') {
    try {
        if (tipo === 'json') {
            localStorage.setItem(clave, JSON.stringify(valor));
        } else {
            localStorage.setItem(clave, valor);
        }
        console.log(`✅ Guardado: ${clave}`);
    } catch (error) {
        console.error(`Error guardando ${clave}:`, error);
    }
}

/**
 * Obtener dato de localStorage
 */
function obtenerDato(clave, tipo = 'json') {
    try {
        const valor = localStorage.getItem(clave);
        if (!valor) return null;
        
        if (tipo === 'json') {
            return JSON.parse(valor);
        } else {
            return valor;
        }
    } catch (error) {
        console.error(`Error obteniendo ${clave}:`, error);
        return null;
    }
}

/**
 * Eliminar dato de localStorage
 */
function eliminarDato(clave) {
    try {
        localStorage.removeItem(clave);
        console.log(`✅ Eliminado: ${clave}`);
    } catch (error) {
        console.error(`Error eliminando ${clave}:`, error);
    }
}

/**
 * Limpiar todo el localStorage (CUIDADO)
 */
function limpiarTodo() {
    try {
        localStorage.clear();
        console.log('✅ localStorage limpiado');
    } catch (error) {
        console.error('Error limpiando localStorage:', error);
    }
}

/**
 * Guardar token
 */
function guardarToken(token) {
    guardarDato(STORAGE_KEYS.TOKEN, token, 'string');
}

/**
 * Obtener token
 */
function obtenerToken() {
    return obtenerDato(STORAGE_KEYS.TOKEN, 'string');
}

/**
 * Guardar usuario
 */
function guardarUsuario(usuario) {
    guardarDato(STORAGE_KEYS.USUARIO, usuario, 'json');
}

/**
 * Obtener usuario
 */
function obtenerUsuario() {
    return obtenerDato(STORAGE_KEYS.USUARIO, 'json');
}

/**
 * Verificar sesión activa
 */
function tieneSesion() {
    return !!obtenerToken() && !!obtenerUsuario();
}

/**
 * Cerrar sesión (eliminar datos de autenticación)
 */
function cerrarSesionLocal() {
    eliminarDato(STORAGE_KEYS.TOKEN);
    eliminarDato(STORAGE_KEYS.USUARIO);
    console.log('✅ Sesión cerrada en cliente');
}

/**
 * Guardar preferencias
 */
function guardarPreferencias(tema, idioma, notificaciones) {
    guardarDato(STORAGE_KEYS.TEMA, tema, 'string');
    guardarDato(STORAGE_KEYS.IDIOMA, idioma, 'string');
    guardarDato(STORAGE_KEYS.NOTIFICACIONES, notificaciones, 'string');
}

/**
 * Obtener preferencias
 */
function obtenerPreferencias() {
    return {
        tema: obtenerDato(STORAGE_KEYS.TEMA, 'string') || 'dark',
        idioma: obtenerDato(STORAGE_KEYS.IDIOMA, 'string') || 'es',
        notificaciones: obtenerDato(STORAGE_KEYS.NOTIFICACIONES, 'string') || 'true'
    };
}

/**
 * Guardar materia seleccionada
 */
function guardarMateriaSeleccionada(materiaId) {
    guardarDato(STORAGE_KEYS.MATERIA_SELECCIONADA, materiaId, 'string');
}

/**
 * Obtener materia seleccionada
 */
function obtenerMateriaSeleccionada() {
    const materia = obtenerDato(STORAGE_KEYS.MATERIA_SELECCIONADA, 'string');
    return materia ? parseInt(materia) : null;
}

/**
 * Guardar progreso del quiz
 */
function guardarProgresoQuiz(datos) {
    guardarDato(STORAGE_KEYS.QUIZ_EN_PROGRESO, datos, 'json');
}

/**
 * Obtener progreso del quiz
 */
function obtenerProgresoQuiz() {
    return obtenerDato(STORAGE_KEYS.QUIZ_EN_PROGRESO, 'json');
}

/**
 * Limpiar progreso del quiz
 */
function limpiarProgresoQuiz() {
    eliminarDato(STORAGE_KEYS.QUIZ_EN_PROGRESO);
}

/**
 * Guardar caché con expiración
 */
function guardarCacheConExpiracion(clave, valor, minutos = 30) {
    const data = {
        valor: valor,
        expiracion: Date.now() + (minutos * 60 * 1000)
    };
    guardarDato(clave, data, 'json');
}

/**
 * Obtener caché (si no está expirado)
 */
function obtenerCache(clave) {
    const data = obtenerDato(clave, 'json');
    if (!data) return null;
    
    if (Date.now() > data.expiracion) {
        eliminarDato(clave);
        return null;
    }
    
    return data.valor;
}

/**
 * Exportar todos los datos (para backup)
 */
function exportarDatos() {
    const datos = {};
    for (let i = 0; i < localStorage.length; i++) {
        const clave = localStorage.key(i);
        datos[clave] = localStorage.getItem(clave);
    }
    return datos;
}

/**
 * Importar datos (restore backup)
 */
function importarDatos(datos) {
    Object.entries(datos).forEach(([clave, valor]) => {
        localStorage.setItem(clave, valor);
    });
    console.log('✅ Datos importados');
}

// Exportar globalmente
window.STORAGE = {
    KEYS: STORAGE_KEYS,
    guardarDato,
    obtenerDato,
    eliminarDato,
    limpiarTodo,
    guardarToken,
    obtenerToken,
    guardarUsuario,
    obtenerUsuario,
    tieneSesion,
    cerrarSesionLocal,
    guardarPreferencias,
    obtenerPreferencias,
    guardarMateriaSeleccionada,
    obtenerMateriaSeleccionada,
    guardarProgresoQuiz,
    obtenerProgresoQuiz,
    limpiarProgresoQuiz,
    guardarCacheConExpiracion,
    obtenerCache,
    exportarDatos,
    importarDatos
};

console.log('✅ localStorage-helper.js listo');