// export-data.js - Exportar datos de BD a CSV/JSON

console.log('✅ export-data.js cargado');

/**
 * Exportar usuarios a CSV
 */
async function exportarUsuariosCSV() {
    try {
        const response = await fetch('/api/usuarios');
        const usuarios = await response.json();
        
        let csv = 'ID,Nombre,Email,Carrera,Racha,Puntos,Correctas,Totales\n';
        
        usuarios.forEach(u => {
            csv += `${u.id},"${u.nombre}","${u.email}",${u.carrera_id},${u.racha_actual},${u.total_puntos},${u.preguntas_correctas},${u.preguntas_totales}\n`;
        });
        
        UTILS.descargarArchivo(csv, 'usuarios.csv', 'text/csv');
        UNIPAZ.mostrarNotificacion('✅ Usuarios exportados a CSV', 'success');
    } catch (error) {
        console.error('Error:', error);
        UNIPAZ.mostrarNotificacion('Error exportando datos', 'error');
    }
}

/**
 * Exportar preguntas a CSV
 */
async function exportarPreguntasCSV() {
    try {
        const response = await fetch('/api/preguntas');
        const preguntas = await response.json();
        
        let csv = 'ID,Texto,OpcionA,OpcionB,OpcionC,OpcionD,Respuesta,Dificultad\n';
        
        preguntas.forEach(p => {
            const texto = `"${p.texto.replace(/"/g, '""')}"`;
            csv += `${p.id},${texto},"${p.opcion_a}","${p.opcion_b}","${p.opcion_c}","${p.opcion_d}",${p.respuesta_correcta},${p.dificultad}\n`;
        });
        
        UTILS.descargarArchivo(csv, 'preguntas.csv', 'text/csv');
        UNIPAZ.mostrarNotificacion('✅ Preguntas exportadas a CSV', 'success');
    } catch (error) {
        console.error('Error:', error);
    }
}

/**
 * Exportar ranking a JSON
 */
async function exportarRankingJSON() {
    try {
        const response = await fetch('/api/rankings/global/racha');
        const rankings = await response.json();
        
        const data = {
            fecha: new Date().toISOString(),
            tipo: 'ranking_racha',
            datos: rankings
        };
        
        UTILS.descargarArchivo(JSON.stringify(data, null, 2), 'ranking.json');
        UNIPAZ.mostrarNotificacion('✅ Ranking exportado a JSON', 'success');
    } catch (error) {
        console.error('Error:', error);
    }
}

/**
 * Generar reporte de estadísticas
 */
async function generarReporteEstadisticas() {
    try {
        const response = await fetch('/api/usuarios');
        const usuarios = await response.json();
        
        const estadisticas = {
            fecha_generacion: new Date().toLocaleString('es-CO'),
            total_usuarios: usuarios.length,
            total_puntos_acumulados: usuarios.reduce((sum, u) => sum + u.total_puntos, 0),
            promedio_puntos: (usuarios.reduce((sum, u) => sum + u.total_puntos, 0) / usuarios.length).toFixed(2),
            racha_promedio: (usuarios.reduce((sum, u) => sum + u.racha_actual, 0) / usuarios.length).toFixed(2),
            usuarios: usuarios
        };
        
        UTILS.descargarArchivo(JSON.stringify(estadisticas, null, 2), 'reporte_estadisticas.json');
        UNIPAZ.mostrarNotificacion('✅ Reporte generado', 'success');
    } catch (error) {
        console.error('Error:', error);
    }
}

window.EXPORT = {
    exportarUsuariosCSV,
    exportarPreguntasCSV,
    exportarRankingJSON,
    generarReporteEstadisticas
};

console.log('✅ export-data.js listo');