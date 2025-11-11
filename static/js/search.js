// search.js - Sistema de búsqueda UNIPAZ

console.log('✅ search.js cargado');

/**
 * Buscar usuarios
 */
async function buscarUsuarios(termino) {
    try {
        const response = await fetch(`/api/usuarios?buscar=${termino}`);
        const usuarios = await response.json();
        return usuarios;
    } catch (error) {
        console.error('Error buscando usuarios:', error);
        return [];
    }
}

/**
 * Buscar preguntas
 */
async function buscarPreguntas(termino, materiaId) {
    try {
        const url = materiaId 
            ? `/api/preguntas/${materiaId}?buscar=${termino}`
            : `/api/preguntas?buscar=${termino}`;
        
        const response = await fetch(url);
        const preguntas = await response.json();
        return preguntas;
    } catch (error) {
        console.error('Error buscando preguntas:', error);
        return [];
    }
}

/**
 * Búsqueda global en tiempo real
 */
function busquedaGlobalTiempoReal(termino, callback) {
    const terminoLower = termino.toLowerCase();
    
    if (terminoLower.length < 2) {
        callback([]);
        return;
    }
    
    // Búsqueda local en elementos de la página
    const elementos = document.querySelectorAll('[data-searchable]');
    const resultados = [];
    
    elementos.forEach(el => {
        const texto = el.textContent.toLowerCase();
        if (texto.includes(terminoLower)) {
            resultados.push({
                titulo: el.getAttribute('data-title') || 'Sin título',
                url: el.getAttribute('data-url') || '#',
                tipo: el.getAttribute('data-type') || 'general',
                elemento: el
            });
        }
    });
    
    callback(resultados);
}

/**
 * Mostrar resultados de búsqueda
 */
function mostrarResultadosBusqueda(resultados) {
    const contenedor = document.getElementById('searchResults');
    if (!contenedor) return;
    
    if (resultados.length === 0) {
        contenedor.innerHTML = '<p class="sin-resultados">No se encontraron resultados</p>';
        return;
    }
    
    let html = '<div class="resultados-lista">';
    
    resultados.forEach(resultado => {
        html += `
            <div class="resultado-item" onclick="navegarA('${resultado.url}')">
                <div class="resultado-tipo">${resultado.tipo}</div>
                <div class="resultado-titulo">${resultado.titulo}</div>
            </div>
        `;
    });
    
    html += '</div>';
    contenedor.innerHTML = html;
}

/**
 * Filtrado avanzado
 */
function filtradoAvanzado(items, filtros) {
    return items.filter(item => {
        // Filtro por nombre/texto
        if (filtros.busqueda) {
            const coincide = item.nombre?.toLowerCase().includes(filtros.busqueda.toLowerCase()) ||
                           item.texto?.toLowerCase().includes(filtros.busqueda.toLowerCase()) ||
                           item.email?.toLowerCase().includes(filtros.busqueda.toLowerCase());
            if (!coincide) return false;
        }
        
        // Filtro por categoría
        if (filtros.categoria && item.categoria !== filtros.categoria) {
            return false;
        }
        
        // Filtro por rango de valores
        if (filtros.minValor && item.valor < filtros.minValor) {
            return false;
        }
        if (filtros.maxValor && item.valor > filtros.maxValor) {
            return false;
        }
        
        // Filtro por estado
        if (filtros.estado && item.estado !== filtros.estado) {
            return false;
        }
        
        return true;
    });
}

/**
 * Ordenar resultados
 */
function ordenarResultados(items, campo, ascendente = true) {
    return items.sort((a, b) => {
        const valA = a[campo];
        const valB = b[campo];
        
        if (typeof valA === 'string') {
            return ascendente 
                ? valA.localeCompare(valB)
                : valB.localeCompare(valA);
        }
        
        return ascendente ? valA - valB : valB - valA;
    });
}

/**
 * Paginación
 */
function paginar(items, pagina = 1, porPagina = 10) {
    const inicio = (pagina - 1) * porPagina;
    const fin = inicio + porPagina;
    
    return {
        items: items.slice(inicio, fin),
        total: items.length,
        paginas: Math.ceil(items.length / porPagina),
        paginaActual: pagina,
        porPagina: porPagina
    };
}

/**
 * Crear widget de búsqueda
 */
function crearWidgetBusqueda(id, opciones = {}) {
    const container = document.getElementById(id);
    if (!container) return;
    
    const placeholder = opciones.placeholder || 'Buscar...';
    const onSearch = opciones.onSearch || (() => {});
    
    const html = `
        <div class="search-widget">
            <div class="search-input-group">
                <input 
                    type="text" 
                    class="search-input" 
                    placeholder="${placeholder}"
                    id="searchInput_${id}"
                >
                <button class="search-btn" onclick="realizarBusqueda_${id}()">
                    🔍
                </button>
            </div>
            <div class="search-filters" id="searchFilters_${id}"></div>
            <div class="search-results" id="searchResults_${id}"></div>
        </div>
    `;
    
    container.innerHTML = html;
    
    // Event listener
    const input = document.getElementById(`searchInput_${id}`);
    input?.addEventListener('keyup', (e) => {
        if (e.key === 'Enter') {
            onSearch(e.target.value);
        }
    });
}

/**
 * Exportar resultados de búsqueda
 */
function exportarResultadosBusqueda(resultados, formato = 'csv') {
    if (formato === 'csv') {
        let csv = 'Tipo,Título,URL\n';
        resultados.forEach(r => {
            csv += `"${r.tipo}","${r.titulo}","${r.url}"\n`;
        });
        UTILS.descargarArchivo(csv, 'resultados-busqueda.csv');
    } else if (formato === 'json') {
        UTILS.descargarArchivo(JSON.stringify(resultados, null, 2), 'resultados-busqueda.json');
    }
}

// Exportar globalmente
window.SEARCH = {
    buscarUsuarios,
    buscarPreguntas,
    busquedaGlobalTiempoReal,
    mostrarResultadosBusqueda,
    filtradoAvanzado,
    ordenarResultados,
    paginar,
    crearWidgetBusqueda,
    exportarResultadosBusqueda
};

console.log('✅ search.js listo');