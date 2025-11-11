// auth.js - Autenticación y Sesión UNIPAZ

console.log('✅ auth.js cargado');

// ===== VARIABLES GLOBALES =====

let usuarioActual = null;
let tokenActual = null;

// ===== AUTENTICACIÓN =====

/**
 * Iniciar sesión
 */
async function iniciarSesion(email, password) {
    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            tokenActual = data.token;
            usuarioActual = data.usuario;
            
            // Guardar en localStorage
            localStorage.setItem('token', tokenActual);
            localStorage.setItem('usuario', JSON.stringify(usuarioActual));
            
            UNIPAZ.CONFIG.usuarioId = usuarioActual.id;
            
            console.log('✅ Sesión iniciada:', usuarioActual);
            UNIPAZ.mostrarNotificacion(`¡Bienvenido, ${usuarioActual.nombre}!`, 'success');
            
            return true;
        } else {
            UNIPAZ.mostrarNotificacion(data.error || 'Error en login', 'error');
        }
    } catch (error) {
        console.error('Error en iniciarSesion:', error);
        UNIPAZ.mostrarNotificacion('Error de conexión', 'error');
    }
    return false;
}

/**
 * Registrarse
 */
async function registrarse(datos) {
    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(datos)
        });

        const data = await response.json();

        if (response.ok) {
            UNIPAZ.mostrarNotificacion('¡Registro exitoso! Inicia sesión.', 'success');
            return true;
        } else {
            UNIPAZ.mostrarNotificacion(data.error || 'Error en registro', 'error');
        }
    } catch (error) {
        console.error('Error en registrarse:', error);
    }
    return false;
}

/**
 * Cerrar sesión
 */
async function cerrarSesion() {
    try {
        await fetch('/api/logout', { method: 'POST' });
        
        localStorage.removeItem('token');
        localStorage.removeItem('usuario');
        
        usuarioActual = null;
        tokenActual = null;
        
        UNIPAZ.mostrarNotificacion('Sesión cerrada', 'success');
        window.location.href = '/login';
    } catch (error) {
        console.error('Error cerrando sesión:', error);
    }
}

/**
 * Verificar si está autenticado
 */
function estaAutenticado() {
    tokenActual = localStorage.getItem('token');
    usuarioActual = JSON.parse(localStorage.getItem('usuario') || 'null');
    
    return !!tokenActual && !!usuarioActual;
}

/**
 * Obtener usuario actual
 */
function obtenerUsuarioActual() {
    if (!estaAutenticado()) {
        return null;
    }
    return usuarioActual;
}

/**
 * Obtener token
 */
function obtenerToken() {
    return localStorage.getItem('token');
}

/**
 * Renovar contraseña
 */
async function renovarContrasena(emailOrId, emailNuevo, contrasenaActual, contrasenaNueva) {
    try {
        const response = await fetch('/api/cambiar-contrasena', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${obtenerToken()}`
            },
            body: JSON.stringify({
                emailOrId,
                emailNuevo,
                contrasenaActual,
                contrasenaNueva
            })
        });

        const data = await response.json();

        if (response.ok) {
            UNIPAZ.mostrarNotificacion('Contraseña actualizada', 'success');
            return true;
        } else {
            UNIPAZ.mostrarNotificacion(data.error || 'Error al cambiar contraseña', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
    }
    return false;
}

/**
 * Recuperar contraseña
 */
async function recuperarContrasena(email) {
    try {
        const response = await fetch('/api/recuperar-contrasena', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email })
        });

        const data = await response.json();

        if (response.ok) {
            UNIPAZ.mostrarNotificacion('Revisa tu email para recuperar acceso', 'success');
            return true;
        } else {
            UNIPAZ.mostrarNotificacion(data.error || 'Error', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
    }
    return false;
}

/**
 * Verificar permisos (Admin)
 */
function esAdmin() {
    return usuarioActual && usuarioActual.rol === 'admin';
}

/**
 * Verificar permisos (Profesor)
 */
function esProfesor() {
    return usuarioActual && usuarioActual.rol === 'profesor';
}

/**
 * Redireccionar si no autenticado
 */
function protegerRuta() {
    if (!estaAutenticado()) {
        window.location.href = '/login';
    }
}

/**
 * Proteger rutas admin
 */
function protegerAdmin() {
    if (!estaAutenticado() || !esAdmin()) {
        window.location.href = '/';
    }
}

// ===== INICIALIZACIÓN =====

document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ auth.js inicializado');
    
    // Verificar autenticación
    if (estaAutenticado()) {
        console.log('✅ Usuario autenticado:', usuarioActual);
        
        // Mostrar nombre en sidebar
        const nombreEl = document.querySelector('[data-usuario-nombre]');
        if (nombreEl) {
            nombreEl.textContent = usuarioActual.nombre;
        }
    } else {
        // Redirigir a login si está en ruta protegida
        const rutasProtegidas = ['/dashboard', '/admin', '/mis-datos'];
        if (rutasProtegidas.some(r => window.location.pathname.includes(r))) {
            window.location.href = '/login';
        }
    }
});

// Exportar globalmente
window.AUTH = {
    iniciarSesion,
    registrarse,
    cerrarSesion,
    estaAutenticado,
    obtenerUsuarioActual,
    obtenerToken,
    renovarContrasena,
    recuperarContrasena,
    esAdmin,
    esProfesor,
    protegerRuta,
    protegerAdmin
};

console.log('✅ auth.js listo para usar');