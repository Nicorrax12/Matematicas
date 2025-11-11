// api-config.js - Configuración centralizada de API

const API_CONFIG = {
    // Base URL
    BASE_URL: 'http://localhost:5000',
    API_URL: 'http://localhost:5000/api',
    
    // Endpoints
    ENDPOINTS: {
        // Autenticación
        LOGIN: '/login',
        REGISTER: '/register',
        LOGOUT: '/logout',
        REFRESH_TOKEN: '/refresh-token',
        
        // Usuarios
        USUARIOS: '/usuarios',
        USUARIO_ID: (id) => `/usuarios/${id}`,
        USUARIO_PERFIL: (id) => `/usuarios/${id}/perfil`,
        USUARIO_ESTADISTICAS: (id) => `/usuarios/${id}/estadisticas`,
        USUARIO_HISTORIAL: (id) => `/usuarios/${id}/historial`,
        
        // Rankings
        RANKING_RACHA_GLOBAL: '/rankings/global/racha',
        RANKING_PORCENTAJE_GLOBAL: '/rankings/global/porcentaje',
        RANKING_MATERIA_RACHA: (id) => `/rankings/materia/${id}/racha`,
        RANKING_MATERIA_PORCENTAJE: (id) => `/rankings/materia/${id}/porcentaje`,
        
        // Materias
        MATERIAS: '/materias',
        MATERIA_ID: (id) => `/materias/${id}`,
        
        // Preguntas
        PREGUNTAS: (materiaId) => `/preguntas/${materiaId}`,
        SIGUIENTE_PREGUNTA: '/quiz/siguiente',
        
        // Quiz
        QUIZ_RESPONDER: '/quiz/responder',
        
        // Carreras
        CARRERAS: '/carreras',
        
        // Concursos
        CONCURSOS_ACTIVOS: '/concursos/activos',
        CONCURSO_ID: (id) => `/concursos/${id}`,
        CONCURSO_BRACKET: (id) => `/concursos/${id}/bracket`,
        CONCURSO_INSCRIBIRSE: (id) => `/concursos/${id}/inscribirse`,
        
        // Logros
        LOGROS_USUARIO: (id) => `/logros/usuario/${id}`,
        LOGRO_VERIFICAR: (id) => `/logros/verificar/${id}`,
        
        // Health
        HEALTH: '/health'
    },
    
    // Timeouts
    TIMEOUT: 30000,
    RETRY_ATTEMPTS: 3,
    RETRY_DELAY: 1000,
    
    // Headers por defecto
    HEADERS: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
    
    // Status codes
    STATUS_CODES: {
        OK: 200,
        CREATED: 201,
        BAD_REQUEST: 400,
        UNAUTHORIZED: 401,
        FORBIDDEN: 403,
        NOT_FOUND: 404,
        CONFLICT: 409,
        SERVER_ERROR: 500
    }
};

/**
 * Obtener URL completa del endpoint
 */
function obtenerURLEndpoint(endpoint) {
    if (endpoint.startsWith('http')) return endpoint;
    return API_CONFIG.API_URL + endpoint;
}

/**
 * Realizar llamada a API con retry
 */
async function llamarAPI(endpoint, opciones = {}) {
    let intentos = 0;
    const maxIntentos = opciones.reintentos || API_CONFIG.RETRY_ATTEMPTS;
    
    while (intentos < maxIntentos) {
        try {
            const url = obtenerURLEndpoint(endpoint);
            const config = {
                ...opciones,
                headers: {
                    ...API_CONFIG.HEADERS,
                    ...opciones.headers
                }
            };
            
            const response = await fetch(url, config);
            return response;
        } catch (error) {
            intentos++;
            if (intentos >= maxIntentos) throw error;
            await new Promise(r => setTimeout(r, API_CONFIG.RETRY_DELAY));
        }
    }
}

// Exportar globalmente
window.API_CONFIG = API_CONFIG;
window.obtenerURLEndpoint = obtenerURLEndpoint;
window.llamarAPI = llamarAPI;

console.log('✅ api-config.js cargado');