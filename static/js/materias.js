// materias.js - Gestión de Materias UNIPAZ

console.log('✅ materias.js cargado');

/**
 * Cargar todas las materias
 */
async function cargarMaterias() {
    try {
        const response = await fetch('/api/materias');
        const materias = await response.json();
        mostrarMaterias(materias);
        console.log('Materias cargadas:', materias);
    } catch (error) {
        console.error('Error cargando materias:', error);
        UNIPAZ.mostrarNotificacion('Error al cargar materias', 'error');
    }
}

/**
 * Mostrar materias en la página
 */
function mostrarMaterias(materias) {
    const contenedor = document.getElementById('materiasContainer');
    if (!contenedor) return;

    let html = '<div class="materias-grid">';
    
    materias.forEach(materia => {
        html += `
            <div class="materia-card" onclick="seleccionarMateria(${materia.id})">
                <div class="materia-icon">📚</div>
                <h3>${materia.nombre}</h3>
                <p>Carrera: ${materia.carrera_id}</p>
                <button class="btn btn-primary" onclick="event.stopPropagation(); iniciarQuiz(${materia.id})">
                    Empezar Quiz
                </button>
            </div>
        `;
    });
    
    html += '</div>';
    contenedor.innerHTML = html;
}

/**
 * Seleccionar una materia
 */
function seleccionarMateria(materiaId) {
    console.log('Materia seleccionada:', materiaId);
    localStorage.setItem('materiaSel', materiaId);
    UNIPAZ.mostrarNotificacion('Materia seleccionada', 'success', 1000);
}

/**
 * Iniciar quiz de una materia
 */
function iniciarQuiz(materiaId) {
    localStorage.setItem('materiaId', materiaId);
    window.location.href = `/quiz?materia=${materiaId}`;
}

/**
 * Filtrar materias por carrera
 */
function filtrarPorCarrera(carreraId) {
    if (carreraId === 'todos') {
        cargarMaterias();
        return;
    }

    const cards = document.querySelectorAll('.materia-card');
    cards.forEach(card => {
        const carrera = card.dataset.carrera;
        if (carrera === carreraId.toString()) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}

/**
 * Buscar materias
 */
function buscarMaterias(termino) {
    const cards = document.querySelectorAll('.materia-card');
    const termino_lower = termino.toLowerCase();

    cards.forEach(card => {
        const nombre = card.querySelector('h3').textContent.toLowerCase();
        if (nombre.includes(termino_lower)) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}

/**
 * Obtener materias por carrera
 */
async function obtenerMateriasPorCarrera(carreraId) {
    try {
        const response = await fetch(`/api/carreras/${carreraId}/materias`);
        const materias = await response.json();
        return materias;
    } catch (error) {
        console.error('Error:', error);
        return [];
    }
}

/**
 * Obtener próxima materia
 */
function obtenerSiguienteMateria() {
    const materiaId = localStorage.getItem('materiaId');
    return materiaId ? parseInt(materiaId) : null;
}

window.MATERIAS = {
    cargarMaterias,
    mostrarMaterias,
    seleccionarMateria,
    iniciarQuiz,
    filtrarPorCarrera,
    buscarMaterias,
    obtenerMateriasPorCarrera,
    obtenerSiguienteMateria
};

console.log('✅ materias.js listo');