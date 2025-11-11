// main.js - JavaScript Principal UNIPAZ Quiz System

console.log('✅ Sistema de Exámenes UNIPAZ Cargado');

// ===== CONFIG GLOBAL =====
const CONFIG = {
    apiUrl: 'http://localhost:5000/api',
    usuarioId: 1,
    modo: 'normal'
};

// ===== UTILIDADES =====

/**
 * Realizar petición fetch a la API
 */
async function apiCall(endpoint, options = {}) {
    const url = `${CONFIG.apiUrl}${endpoint}`;
    const config = {
        headers: {
            'Content-Type': 'application/json',
            ...options.headers
        },
        ...options
    };
    
    try {
        const response = await fetch(url, config);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        mostrarNotificacion('Error en la conexión', 'error');
        return null;
    }
}

/**
 * Mostrar notificación al usuario
 */
function mostrarNotificacion(mensaje, tipo = 'info', duracion = 3000) {
    const notificacion = document.createElement('div');
    notificacion.className = `notificacion notificacion-${tipo}`;
    notificacion.textContent = mensaje;
    notificacion.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        background: ${tipo === 'success' ? '#43e97b' : tipo === 'error' ? '#f5576c' : '#667eea'};
        color: white;
        border-radius: 8px;
        font-weight: 600;
        z-index: 10000;
        animation: slideInRight 0.3s ease;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    `;
    
    document.body.appendChild(notificacion);
    
    setTimeout(() => {
        notificacion.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => notificacion.remove(), 300);
    }, duracion);
}

/**
 * Formatear número a formato legible
 */
function formatearNumero(num) {
    return new Intl.NumberFormat('es-CO').format(num);
}

/**
 * Formatear fecha
 */
function formatearFecha(fecha) {
    return new Date(fecha).toLocaleDateString('es-CO');
}

/**
 * Guardar en localStorage
 */
function guardarLocal(clave, valor) {
    localStorage.setItem(clave, JSON.stringify(valor));
}

/**
 * Obtener de localStorage
 */
function obtenerLocal(clave) {
    const valor = localStorage.getItem(clave);
    return valor ? JSON.parse(valor) : null;
}

// ===== AUTENTICACIÓN =====

/**
 * Verificar sesión del usuario
 */
function verificarSesion() {
    const usuario = obtenerLocal('usuario');
    if (!usuario) {
        console.warn('No hay sesión activa');
        return false;
    }
    CONFIG.usuarioId = usuario.id;
    return true;
}

/**
 * Cerrar sesión
 */
function cerrarSesion() {
    localStorage.removeItem('usuario');
    localStorage.removeItem('token');
    window.location.href = '/login';
}

// ===== RANKINGS =====

/**
 * Cargar rankings globales
 */
async function cargarRankings() {
    console.log('Cargando rankings...');
    
    try {
        const [rachas, porcentajes] = await Promise.all([
            apiCall('/rankings/global/racha'),
            apiCall('/rankings/global/porcentaje')
        ]);
        
        if (rachas && porcentajes) {
            console.log('Rankings cargados:', { rachas, porcentajes });
            return { rachas, porcentajes };
        }
    } catch (error) {
        console.error('Error cargando rankings:', error);
    }
    return null;
}

/**
 * Cargar rankings por materia
 */
async function cargarRankingsPorMateria(materiaId) {
    console.log(`Cargando rankings para materia ${materiaId}...`);
    
    try {
        const [rachas, porcentajes] = await Promise.all([
            apiCall(`/rankings/materia/${materiaId}/racha`),
            apiCall(`/rankings/materia/${materiaId}/porcentaje`)
        ]);
        
        return { rachas, porcentajes };
    } catch (error) {
        console.error('Error cargando rankings por materia:', error);
    }
    return null;
}

// ===== CONCURSOS =====

/**
 * Cargar concursos activos
 */
async function cargarConcursosActivos() {
    console.log('Cargando concursos activos...');
    const data = await apiCall('/concursos/activos');
    return data;
}

/**
 * Inscribir en concurso
 */
async function inscribirConcurso(concursoId) {
    console.log(`Inscribiendo en concurso ${concursoId}...`);
    
    const data = await apiCall(`/concursos/${concursoId}/inscribirse`, {
        method: 'POST',
        body: JSON.stringify({
            usuario_id: CONFIG.usuarioId
        })
    });
    
    if (data) {
        mostrarNotificacion('¡Inscripción exitosa!', 'success');
        return true;
    }
    return false;
}

/**
 * Obtener bracket de concurso
 */
async function obtenerBracket(concursoId) {
    console.log(`Obteniendo bracket del concurso ${concursoId}...`);
    const data = await apiCall(`/concursos/${concursoId}/bracket`);
    return data;
}

/**
 * Responder pregunta en concurso
 */
async function responderConcurso(concursoId, respuesta) {
    console.log(`Respondiendo en concurso ${concursoId}...`);
    
    const data = await apiCall(`/concursos/${concursoId}/responder`, {
        method: 'POST',
        body: JSON.stringify({
            usuario_id: CONFIG.usuarioId,
            respuesta: respuesta,
            tiempo_respuesta: Math.random() * 30
        })
    });
    
    return data;
}

// ===== LOGROS =====

/**
 * Cargar logros del usuario
 */
async function cargarLogrosUsuario(usuarioId) {
    console.log(`Cargando logros del usuario ${usuarioId}...`);
    const data = await apiCall(`/logros/usuario/${usuarioId}`);
    return data;
}

/**
 * Verificar si se desbloqueó un logro
 */
async function verificarLogro(logrosId) {
    console.log(`Verificando logro ${logrosId}...`);
    
    const data = await apiCall(`/logros/verificar/${logrosId}`, {
        method: 'POST',
        body: JSON.stringify({
            usuario_id: CONFIG.usuarioId
        })
    });
    
    if (data && data.desbloqueado) {
        mostrarNotificacion(`🎖️ ¡Logro desbloqueado: ${data.nombre}!`, 'success');
    }
    
    return data;
}

// ===== USUARIO =====

/**
 * Cargar perfil del usuario
 */
async function cargarPerfil(usuarioId) {
    console.log(`Cargando perfil del usuario ${usuarioId}...`);
    const data = await apiCall(`/usuario/${usuarioId}/perfil`);
    return data;
}

/**
 * Cargar estadísticas del usuario
 */
async function cargarEstadisticas(usuarioId) {
    console.log(`Cargando estadísticas del usuario ${usuarioId}...`);
    const data = await apiCall(`/usuario/${usuarioId}/estadisticas`);
    return data;
}

/**
 * Actualizar perfil del usuario
 */
async function actualizarPerfil(usuarioId, datos) {
    console.log(`Actualizando perfil del usuario ${usuarioId}...`);
    
    const data = await apiCall(`/usuario/${usuarioId}/actualizar`, {
        method: 'PUT',
        body: JSON.stringify(datos)
    });
    
    if (data) {
        mostrarNotificacion('Perfil actualizado correctamente', 'success');
        return true;
    }
    return false;
}

// ===== QUIZ =====

/**
 * Responder pregunta en quiz
 */
async function responderQuiz(preguntaId, respuesta) {
    console.log(`Respondiendo pregunta ${preguntaId}...`);
    
    const data = await apiCall('/quiz/respuesta', {
        method: 'POST',
        body: JSON.stringify({
            usuario_id: CONFIG.usuarioId,
            pregunta_id: preguntaId,
            respuesta_dada: respuesta,
            tiempo_respuesta: Math.random() * 60,
            modo: CONFIG.modo
        })
    });
    
    return data;
}

/**
 * Obtener siguiente pregunta
 */
async function obtenerSiguientePregunta(materiaId) {
    console.log(`Obteniendo siguiente pregunta de materia ${materiaId}...`);
    const data = await apiCall(`/quiz/siguiente-pregunta?materia_id=${materiaId}`);
    return data;
}

// ===== EVENTOS =====

/**
 * Navegar a sección
 */
function navegarA(url) {
    window.location.href = url;
}

/**
 * Animar elemento
 */
function animar(elemento, animacion) {
    elemento.classList.add(`animate-${animacion}`);
    setTimeout(() => {
        elemento.classList.remove(`animate-${animacion}`);
    }, 600);
}

// ===== INICIALIZACIÓN =====

document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ DOM Cargado');
    
    // Verificar sesión
    if (!verificarSesion()) {
        console.warn('Sesión no válida');
    }
    
    // Cargar datos iniciales
    cargarDatosIniciales();
});

/**
 * Cargar datos iniciales
 */
async function cargarDatosIniciales() {
    try {
        console.log('Cargando datos iniciales...');
        // Aquí irían llamadas a datos iniciales
    } catch (error) {
        console.error('Error cargando datos iniciales:', error);
    }
}

// Exportar para uso en otros scripts
window.UNIPAZ = {
    apiCall,
    mostrarNotificacion,
    formatearNumero,
    formatearFecha,
    guardarLocal,
    obtenerLocal,
    verificarSesion,
    cerrarSesion,
    cargarRankings,
    cargarConcursosActivos,
    inscribirConcurso,
    cargarLogrosUsuario,
    cargarPerfil,
    responderQuiz,
    navegarA,
    animar,
    CONFIG
};

console.log('✅ main.js inicializado correctamente');