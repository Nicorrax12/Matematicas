// concursos.js - Lógica de Concursos UNIPAZ

console.log('✅ concursos.js cargado');

// ===== VARIABLES GLOBALES =====

let concursoActual = null;
let participantes = [];
let bracketData = {};

// ===== FUNCIONES CONCURSOS =====

/**
 * Cargar concursos activos
 */
async function cargarConcursosActivos() {
    try {
        const concursos = await UNIPAZ.cargarConcursosActivos();
        
        if (concursos) {
            mostrarConcursos(concursos);
            console.log('Concursos activos cargados:', concursos);
        }
    } catch (error) {
        console.error('Error cargando concursos activos:', error);
        UNIPAZ.mostrarNotificacion('Error al cargar concursos', 'error');
    }
}

/**
 * Mostrar lista de concursos
 */
function mostrarConcursos(concursos) {
    const contenedor = document.getElementById('concursosContainer');
    if (!contenedor) return;

    let html = '';
    
    concursos.forEach(concurso => {
        const badge = getBadgeEstado(concurso.estado);
        
        html += `
            <div class="concurso-card" data-concurso-id="${concurso.id}">
                <div class="concurso-header">
                    <div>
                        <h3>${concurso.nombre}</h3>
                        <p>${concurso.materia}</p>
                    </div>
                    <span class="${badge.clase}">${badge.texto}</span>
                </div>
                <div class="concurso-stats">
                    <div class="stat">
                        <span>Participantes</span>
                        <strong>${concurso.participantes}</strong>
                    </div>
                    <div class="stat">
                        <span>Ronda</span>
                        <strong>${concurso.ronda}</strong>
                    </div>
                </div>
                <div class="concurso-acciones">
                    <button class="btn btn-primary" onclick="verBracket(${concurso.id})">
                        Ver Bracket
                    </button>
                    <button class="btn btn-secondary" onclick="inscribirConcurso(${concurso.id})">
                        Participar
                    </button>
                </div>
            </div>
        `;
    });

    contenedor.innerHTML = html;
}

/**
 * Obtener badge de estado
 */
function getBadgeEstado(estado) {
    const badges = {
        'activo': { clase: 'badge-activo', texto: '🔴 En Vivo' },
        'proximo': { clase: 'badge-proximo', texto: '⏳ Próximamente' },
        'finalizado': { clase: 'badge-finalizado', texto: '✅ Finalizado' }
    };
    return badges[estado] || { clase: 'badge-default', texto: estado };
}

/**
 * Inscribirse en concurso
 */
async function inscribirConcurso(concursoId) {
    try {
        const success = await UNIPAZ.inscribirConcurso(concursoId);
        
        if (success) {
            console.log(`Inscripción exitosa en concurso ${concursoId}`);
            cargarConcursosActivos();
        }
    } catch (error) {
        console.error('Error inscribiendo en concurso:', error);
        UNIPAZ.mostrarNotificacion('Error en la inscripción', 'error');
    }
}

/**
 * Ver bracket del concurso
 */
async function verBracket(concursoId) {
    try {
        concursoActual = concursoId;
        bracketData = await UNIPAZ.obtenerBracket(concursoId);
        
        if (bracketData) {
            mostrarBracketVisual(bracketData);
            console.log('Bracket cargado:', bracketData);
        }
    } catch (error) {
        console.error('Error cargando bracket:', error);
        UNIPAZ.mostrarNotificacion('Error al cargar bracket', 'error');
    }
}

/**
 * Mostrar visualización del bracket
 */
function mostrarBracketVisual(datos) {
    const contenedor = document.getElementById('bracketContainer');
    if (!contenedor) return;

    let html = '<div class="bracket">';
    
    // Rondas
    const rondas = datos.rondas || [];
    rondas.forEach((ronda, index) => {
        html += `<div class="ronda" data-ronda="${index}">`;
        html += `<h4>${ronda.nombre}</h4>`;
        
        // Matchups
        if (ronda.matchups) {
            ronda.matchups.forEach(matchup => {
                html += `
                    <div class="matchup">
                        <div class="jugador ${matchup.ganador === 1 ? 'ganador' : ''}">
                            ${matchup.jugador1.nombre}
                        </div>
                        <div class="vs">VS</div>
                        <div class="jugador ${matchup.ganador === 2 ? 'ganador' : ''}">
                            ${matchup.jugador2.nombre}
                        </div>
                    </div>
                `;
            });
        }
        
        html += '</div>';
    });
    
    html += '</div>';
    contenedor.innerHTML = html;
}

/**
 * Responder en duelo del concurso
 */
async function responderEnDuelo(respuesta) {
    try {
        const resultado = await UNIPAZ.responderConcurso(concursoActual, respuesta);
        
        if (resultado) {
            mostrarResultadoDuelo(resultado);
            console.log('Respuesta registrada:', resultado);
        }
    } catch (error) {
        console.error('Error respondiendo en duelo:', error);
        UNIPAZ.mostrarNotificacion('Error al registrar respuesta', 'error');
    }
}

/**
 * Mostrar resultado del duelo
 */
function mostrarResultadoDuelo(resultado) {
    const mensaje = resultado.ganaste 
        ? '🎉 ¡Ganaste el duelo! Avanzas a la siguiente ronda.'
        : '😢 Perdiste este duelo. Mejor suerte en el próximo concurso.';
    
    UNIPAZ.mostrarNotificacion(mensaje, resultado.ganaste ? 'success' : 'info');
}

/**
 * Crear nuevo concurso (Admin)
 */
async function crearConcurso(datos) {
    try {
        const respuesta = await UNIPAZ.apiCall('/concursos/crear', {
            method: 'POST',
            body: JSON.stringify(datos)
        });
        
        if (respuesta) {
            UNIPAZ.mostrarNotificacion('Concurso creado exitosamente', 'success');
            cargarConcursosActivos();
            return true;
        }
    } catch (error) {
        console.error('Error creando concurso:', error);
        UNIPAZ.mostrarNotificacion('Error al crear concurso', 'error');
    }
    return false;
}

/**
 * Eliminar concurso (Admin)
 */
async function eliminarConcurso(concursoId) {
    if (!confirm('¿Estás seguro de que deseas eliminar este concurso?')) {
        return;
    }
    
    try {
        const respuesta = await UNIPAZ.apiCall(`/concursos/${concursoId}`, {
            method: 'DELETE'
        });
        
        if (respuesta) {
            UNIPAZ.mostrarNotificacion('Concurso eliminado', 'success');
            cargarConcursosActivos();
        }
    } catch (error) {
        console.error('Error eliminando concurso:', error);
    }
}

/**
 * Obtener mi posición en concurso
 */
async function obtenerMiPosicion(concursoId) {
    try {
        const posicion = await UNIPAZ.apiCall(`/concursos/${concursoId}/mi-posicion`);
        return posicion;
    } catch (error) {
        console.error('Error obteniendo posición:', error);
    }
    return null;
}

/**
 * Calcular ganador del concurso (simulación)
 */
function simularTorneo(concursoId) {
    console.log(`Simulando torneo del concurso ${concursoId}`);
    
    // Simular avance
    const rondas = ['Octavos', 'Cuartos', 'Semifinal', 'Final'];
    
    rondas.forEach((ronda, index) => {
        setTimeout(() => {
            UNIPAZ.mostrarNotificacion(`Avanzaste a ${ronda}! 🎉`, 'success');
        }, (index + 1) * 5000);
    });
}

/**
 * Exportar resultados del concurso
 */
function exportarResultados(concursoId) {
    const datos = {
        concursoId,
        fecha: new Date().toLocaleDateString(),
        bracket: bracketData
    };
    
    UTILS.descargarArchivo(JSON.stringify(datos, null, 2), `concurso-${concursoId}.json`);
    UNIPAZ.mostrarNotificacion('Resultados exportados', 'success');
}

/**
 * Filtrar concursos por estado
 */
function filtrarConcursos(estado) {
    const cards = document.querySelectorAll('.concurso-card');
    
    cards.forEach(card => {
        if (estado === 'todos' || card.dataset.estado === estado) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}

/**
 * Obtener estadísticas del concurso
 */
async function obtenerEstadisticasConcurso(concursoId) {
    try {
        const stats = await UNIPAZ.apiCall(`/concursos/${concursoId}/estadisticas`);
        return stats;
    } catch (error) {
        console.error('Error obteniendo estadísticas:', error);
    }
    return null;
}

// ===== INICIALIZACIÓN =====

document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ concursos.js inicializado');
    
    // Cargar concursos iniciales
    cargarConcursosActivos();
    
    // Filtros
    document.querySelectorAll('[data-filter-estado]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            filtrarConcursos(e.target.dataset.filterEstado);
        });
    });
});

// Exportar globalmente
window.CONCURSOS = {
    cargarConcursosActivos,
    mostrarConcursos,
    inscribirConcurso,
    verBracket,
    mostrarBracketVisual,
    responderEnDuelo,
    crearConcurso,
    eliminarConcurso,
    obtenerMiPosicion,
    simularTorneo,
    exportarResultados,
    filtrarConcursos,
    obtenerEstadisticasConcurso
};

console.log('✅ concursos.js listo para usar');