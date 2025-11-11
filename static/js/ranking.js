// ranking.js - Lógica de Rankings UNIPAZ

console.log('✅ ranking.js cargado');

// ===== FUNCIONES RANKING =====

/**
 * Cargar y mostrar rankings globales
 */
async function cargarYMostrarRankings() {
    try {
        const rankings = await UNIPAZ.cargarRankings();
        
        if (rankings) {
            mostrarRankingRachas(rankings.rachas);
            mostrarRankingPorcentaje(rankings.porcentajes);
            console.log('Rankings cargados correctamente');
        }
    } catch (error) {
        console.error('Error en cargarYMostrarRankings:', error);
        UNIPAZ.mostrarNotificacion('Error al cargar rankings', 'error');
    }
}

/**
 * Mostrar tabla de rankings por racha
 */
function mostrarRankingRachas(datos) {
    if (!datos || datos.length === 0) {
        console.warn('No hay datos de rachas');
        return;
    }

    const tabla = document.getElementById('tablaRachitas');
    if (!tabla) return;

    let html = `
        <table>
            <thead>
                <tr>
                    <th>Posición</th>
                    <th>Estudiante</th>
                    <th>Racha</th>
                    <th>Puntos</th>
                </tr>
            </thead>
            <tbody>
    `;

    datos.forEach((usuario, index) => {
        const medalla = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : `${index + 1}`;
        html += `
            <tr>
                <td>${medalla}</td>
                <td>
                    <div class="user-info">
                        <span class="avatar">${usuario.nombre.charAt(0)}</span>
                        <span>${usuario.nombre}</span>
                    </div>
                </td>
                <td>
                    <span class="racha">🔥 ${usuario.racha}</span>
                </td>
                <td>${UNIPAZ.formatearNumero(usuario.puntos)}</td>
            </tr>
        `;
    });

    html += `
            </tbody>
        </table>
    `;

    tabla.innerHTML = html;
}

/**
 * Mostrar tabla de rankings por porcentaje
 */
function mostrarRankingPorcentaje(datos) {
    if (!datos || datos.length === 0) {
        console.warn('No hay datos de porcentajes');
        return;
    }

    const tabla = document.getElementById('tablaPorcentaje');
    if (!tabla) return;

    let html = `
        <table>
            <thead>
                <tr>
                    <th>Posición</th>
                    <th>Estudiante</th>
                    <th>% Éxito</th>
                    <th>Preguntas</th>
                </tr>
            </thead>
            <tbody>
    `;

    datos.forEach((usuario, index) => {
        const medalla = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : `${index + 1}`;
        html += `
            <tr>
                <td>${medalla}</td>
                <td>
                    <div class="user-info">
                        <span class="avatar">${usuario.nombre.charAt(0)}</span>
                        <span>${usuario.nombre}</span>
                    </div>
                </td>
                <td>
                    <span class="porcentaje">${usuario.porcentaje}%</span>
                </td>
                <td>${usuario.preguntas_correctas}/${usuario.preguntas_totales}</td>
            </tr>
        `;
    });

    html += `
            </tbody>
        </table>
    `;

    tabla.innerHTML = html;
}

/**
 * Cargar rankings por materia
 */
async function cargarRankingsPorMateria(materiaId) {
    try {
        const rankings = await UNIPAZ.cargarRankingsPorMateria(materiaId);
        
        if (rankings) {
            console.log('Rankings por materia cargados:', rankings);
            return rankings;
        }
    } catch (error) {
        console.error('Error cargando rankings por materia:', error);
    }
    return null;
}

/**
 * Filtrar rankings por carrera
 */
function filtrarPorCarrera(carreraId) {
    const filas = document.querySelectorAll('tbody tr');
    
    filas.forEach(fila => {
        const carrera = fila.dataset.carrera;
        
        if (carreraId === 'todos' || carrera === carreraId.toString()) {
            fila.style.display = '';
            UNIPAZ.animar(fila, 'fadeIn');
        } else {
            fila.style.display = 'none';
        }
    });
}

/**
 * Ordenar tabla por columna
 */
function ordenarTabla(columna) {
    const tabla = document.querySelector('table tbody');
    const filas = Array.from(tabla.querySelectorAll('tr'));

    filas.sort((a, b) => {
        const aValor = a.children[columna].textContent;
        const bValor = b.children[columna].textContent;

        // Intentar convertir a número si es posible
        const aNum = parseFloat(aValor.replace(/[^0-9.-]/g, ''));
        const bNum = parseFloat(bValor.replace(/[^0-9.-]/g, ''));

        if (!isNaN(aNum) && !isNaN(bNum)) {
            return bNum - aNum; // Orden descendente para números
        }

        return aValor.localeCompare(bValor); // Orden alfabético
    });

    tabla.innerHTML = '';
    filas.forEach(fila => tabla.appendChild(fila));
}

/**
 * Actualizar rankings en tiempo real
 */
function actualizarRankingsEnTiempoReal() {
    setInterval(() => {
        cargarYMostrarRankings();
        console.log('Rankings actualizados');
    }, 30000); // Cada 30 segundos
}

/**
 * Obtener puesto del usuario actual
 */
async function obtenerPuestoUsuario() {
    try {
        const rankings = await UNIPAZ.cargarRankings();
        const usuarioId = UNIPAZ.CONFIG.usuarioId;

        // Buscar en rachas
        let puesto = rankings.rachas.findIndex(u => u.id === usuarioId) + 1;
        
        if (puesto > 0) {
            console.log(`Tu posición en rachas: ${puesto}`);
            return {
                racha: puesto,
                porcentaje: rankings.porcentajes.findIndex(u => u.id === usuarioId) + 1
            };
        }
    } catch (error) {
        console.error('Error obteniendo puesto del usuario:', error);
    }
    return null;
}

/**
 * Crear badge de medalla
 */
function crearBadgeMedalla(posicion) {
    const badges = {
        1: '🥇 Oro',
        2: '🥈 Plata',
        3: '🥉 Bronce'
    };

    if (badges[posicion]) {
        return `<span class="badge badge-${posicion}">${badges[posicion]}</span>`;
    }
    return `<span class="badge">#${posicion}</span>`;
}

/**
 * Exportar datos de ranking a CSV
 */
function exportarRankingCSV() {
    const tabla = document.querySelector('table');
    if (!tabla) return;

    let csv = 'Posición,Estudiante,Valor\n';
    
    tabla.querySelectorAll('tbody tr').forEach((fila, index) => {
        const celdas = fila.querySelectorAll('td');
        const posicion = index + 1;
        const estudiante = celdas[1]?.textContent.trim() || '';
        const valor = celdas[2]?.textContent.trim() || '';
        
        csv += `${posicion},"${estudiante}","${valor}"\n`;
    });

    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'ranking-unipaz.csv';
    a.click();
    window.URL.revokeObjectURL(url);

    UNIPAZ.mostrarNotificacion('Ranking exportado a CSV', 'success');
}

/**
 * Compartir ranking en redes
 */
function compartirRanking(plataforma) {
    const usuario = UNIPAZ.CONFIG.usuarioId;
    const mensaje = encodeURIComponent(`¡Estoy en el ranking de UNIPAZ! 🏆 #UnipazQuiz`);
    
    const urls = {
        twitter: `https://twitter.com/intent/tweet?text=${mensaje}`,
        facebook: `https://www.facebook.com/sharer/sharer.php?u=${window.location.href}`,
        whatsapp: `https://wa.me/?text=${mensaje}`
    };

    if (urls[plataforma]) {
        window.open(urls[plataforma], '_blank');
    }
}

// ===== INICIALIZACIÓN =====

document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ ranking.js inicializado');
    
    // Cargar rankings iniciales
    cargarYMostrarRankings();
    
    // Actualizar cada 30 segundos
    actualizarRankingsEnTiempoReal();
    
    // Agregar event listeners a botones
    document.querySelectorAll('[data-filter-carrera]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            filtrarPorCarrera(e.target.dataset.filterCarrera);
        });
    });
});

// Exportar globalmente
window.RANKING = {
    cargarYMostrarRankings,
    mostrarRankingRachas,
    mostrarRankingPorcentaje,
    cargarRankingsPorMateria,
    filtrarPorCarrera,
    ordenarTabla,
    obtenerPuestoUsuario,
    crearBadgeMedalla,
    exportarRankingCSV,
    compartirRanking
};

console.log('✅ ranking.js listo para usar');