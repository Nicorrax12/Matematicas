// analytics.js - Sistema de análisis y estadísticas

console.log('✅ analytics.js cargado');

class Analytics {
    constructor() {
        this.eventos = [];
        this.sesionInicio = Date.now();
    }

    /**
     * Registrar evento
     */
    evento(nombre, datos = {}) {
        const evento = {
            nombre,
            datos,
            timestamp: new Date(),
            url: window.location.pathname,
            userAgent: navigator.userAgent
        };

        this.eventos.push(evento);
        console.log(`📊 Evento registrado: ${nombre}`, datos);

        // Enviar a servidor si se desea (comentado)
        // this.enviarAlServidor(evento);
    }

    /**
     * Evento: Usuario completa quiz
     */
    quizCompletado(materiaId, modo, puntos, porcentaje) {
        this.evento('quiz_completado', {
            materiaId,
            modo,
            puntos,
            porcentaje,
            duracion: Date.now() - this.sesionInicio
        });
    }

    /**
     * Evento: Usuario responde pregunta
     */
    preguntaRespondida(preguntaId, correcta, tiempo) {
        this.evento('pregunta_respondida', {
            preguntaId,
            correcta,
            tiempo
        });
    }

    /**
     * Evento: Usuario participa en concurso
     */
    concursoParticipado(concursoId, resultado) {
        this.evento('concurso_participado', {
            concursoId,
            resultado
        });
    }

    /**
     * Evento: Usuario desbloquea logro
     */
    logroDesbloqueado(logroId, nombre) {
        this.evento('logro_desbloqueado', {
            logroId,
            nombre
        });
    }

    /**
     * Obtener resumen de sesión
     */
    resumenSesion() {
        const duracion = Date.now() - this.sesionInicio;
        const quizCompletados = this.eventos.filter(e => e.nombre === 'quiz_completado').length;
        const preguntasRespondidas = this.eventos.filter(e => e.nombre === 'pregunta_respondida').length;
        const logrosDesbloqueados = this.eventos.filter(e => e.nombre === 'logro_desbloqueado').length;

        return {
            duracion: Math.round(duracion / 1000), // segundos
            quizCompletados,
            preguntasRespondidas,
            logrosDesbloqueados,
            totalEventos: this.eventos.length
        };
    }

    /**
     * Exportar eventos
     */
    exportarEventos(formato = 'json') {
        const resumen = this.resumenSesion();
        
        const datos = {
            resumen,
            eventos: this.eventos
        };

        if (formato === 'json') {
            UTILS.descargarArchivo(JSON.stringify(datos, null, 2), 'analytics.json');
        } else if (formato === 'csv') {
            let csv = 'Nombre,Timestamp,URL,Datos\n';
            this.eventos.forEach(e => {
                csv += `"${e.nombre}","${e.timestamp}","${e.url}","${JSON.stringify(e.datos)}"\n`;
            });
            UTILS.descargarArchivo(csv, 'analytics.csv');
        }
    }

    /**
     * Limpiar eventos
     */
    limpiar() {
        this.eventos = [];
        this.sesionInicio = Date.now();
    }

    /**
     * Obtener estadísticas por tipo
     */
    estadisticasPorTipo() {
        const stats = {};

        this.eventos.forEach(e => {
            if (!stats[e.nombre]) {
                stats[e.nombre] = 0;
            }
            stats[e.nombre]++;
        });

        return stats;
    }

    /**
     * Enviar eventos al servidor (implementar según necesidad)
     */
    async enviarAlServidor(evento) {
        try {
            await fetch('/api/analytics', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(evento)
            });
        } catch (error) {
            console.error('Error enviando analytics:', error);
        }
    }
}

// Crear instancia global
window.ANALYTICS = new Analytics();

// Registrar eventos automáticamente
document.addEventListener('click', (e) => {
    if (e.target.dataset.track) {
        ANALYTICS.evento(`click_${e.target.dataset.track}`);
    }
});

console.log('✅ analytics.js listo');