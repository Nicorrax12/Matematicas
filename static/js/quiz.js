// quiz.js - Lógica de Quiz UNIPAZ

console.log('✅ quiz.js cargado');

// ===== VARIABLES GLOBALES =====

let quizActual = {
    modo: 'normal',
    materiaId: null,
    preguntaActual: 0,
    preguntas: [],
    respuestas: [],
    puntos: 0,
    racha: 0,
    tiempoInicio: null
};

let timerInterval = null;

// ===== FUNCIONES QUIZ =====

/**
 * Iniciar quiz
 */
async function iniciarQuiz(modo, materiaId) {
    try {
        quizActual.modo = modo;
        quizActual.materiaId = materiaId;
        quizActual.preguntaActual = 0;
        quizActual.respuestas = [];
        quizActual.puntos = 0;
        quizActual.racha = 0;
        quizActual.tiempoInicio = Date.now();
        
        console.log(`Iniciando quiz ${modo} para materia ${materiaId}`);
        
        // Cargar preguntas
        await cargarPreguntas(materiaId, modo);
        mostrarPregunta();
        
        UNIPAZ.mostrarNotificacion(`Quiz iniciado en modo ${modo}`, 'success');
    } catch (error) {
        console.error('Error iniciando quiz:', error);
        UNIPAZ.mostrarNotificacion('Error al iniciar quiz', 'error');
    }
}

/**
 * Cargar preguntas
 */
async function cargarPreguntas(materiaId, modo) {
    try {
        const dificultad = modo === 'hardcore' ? 'dificil' : 'medio';
        const cantidad = modo === 'pesadilla' ? 10 : 100;
        
        const preguntas = await UNIPAZ.apiCall(
            `/quiz/preguntas/${materiaId}?dificultad=${dificultad}&cantidad=${cantidad}`
        );
        
        if (preguntas) {
            quizActual.preguntas = preguntas;
            console.log(`${preguntas.length} preguntas cargadas`);
        }
    } catch (error) {
        console.error('Error cargando preguntas:', error);
    }
}

/**
 * Mostrar pregunta actual
 */
function mostrarPregunta() {
    const pregunta = quizActual.preguntas[quizActual.preguntaActual];
    
    if (!pregunta) {
        finalizarQuiz();
        return;
    }
    
    const contenedor = document.getElementById('preguntaContainer');
    if (!contenedor) return;
    
    let html = `
        <div class="pregunta-header">
            <div class="progreso">
                <span>${quizActual.preguntaActual + 1}/${quizActual.preguntas.length}</span>
                <div class="barra-progreso">
                    <div class="relleno" style="width: ${((quizActual.preguntaActual + 1) / quizActual.preguntas.length) * 100}%"></div>
                </div>
            </div>
            <div class="stats">
                <span class="puntos">💰 ${quizActual.puntos}</span>
                <span class="racha">🔥 ${quizActual.racha}</span>
            </div>
        </div>
        
        <div class="pregunta-contenido">
            <div class="pregunta-texto">
                ${pregunta.texto}
            </div>
            
            ${pregunta.imagen ? `<img src="${pregunta.imagen}" class="pregunta-imagen">` : ''}
            
            <div class="opciones">
                ${['a', 'b', 'c', 'd'].map(letra => `
                    <button class="opcion-btn" onclick="responderPregunta('${letra}')" data-opcion="${letra}">
                        <span class="letra">${letra.toUpperCase()})</span>
                        <span class="texto">${pregunta.opciones[letra]}</span>
                    </button>
                `).join('')}
            </div>
        </div>
    `;
    
    contenedor.innerHTML = html;
    iniciarTimer();
}

/**
 * Responder pregunta
 */
async function responderPregunta(opcion) {
    if (timerInterval) {
        clearInterval(timerInterval);
    }
    
    const pregunta = quizActual.preguntas[quizActual.preguntaActual];
    
    try {
        const resultado = await UNIPAZ.apiCall('/quiz/responder', {
            method: 'POST',
            body: JSON.stringify({
                usuario_id: UNIPAZ.CONFIG.usuarioId,
                pregunta_id: pregunta.id,
                respuesta_dada: opcion,
                tiempo_respuesta: UTILS.formatearTiempo(Date.now() - quizActual.tiempoInicio),
                modo: quizActual.modo
            })
        });
        
        if (resultado) {
            registrarRespuesta(opcion, resultado.correcta, resultado.puntos_ganados);
            
            if (quizActual.modo === 'pesadilla' && !resultado.correcta) {
                finalizarQuizPesadilla();
                return;
            }
            
            setTimeout(() => {
                quizActual.preguntaActual++;
                mostrarPregunta();
            }, 2000);
        }
    } catch (error) {
        console.error('Error respondiendo pregunta:', error);
    }
}

/**
 * Registrar respuesta
 */
function registrarRespuesta(respuesta, correcta, puntos) {
    quizActual.respuestas.push({
        pregunta: quizActual.preguntaActual,
        respuesta,
        correcta,
        puntos
    });
    
    if (correcta) {
        quizActual.racha++;
        quizActual.puntos += puntos;
        UNIPAZ.mostrarNotificacion('✅ ¡Correcto!', 'success', 1000);
    } else {
        quizActual.racha = 0;
        UNIPAZ.mostrarNotificacion('❌ Incorrecto', 'info', 1000);
    }
}

/**
 * Iniciar temporizador
 */
function iniciarTimer() {
    let segundos = 60;
    const timerEl = document.getElementById('timer');
    
    if (timerInterval) {
        clearInterval(timerInterval);
    }
    
    timerInterval = setInterval(() => {
        segundos--;
        
        if (timerEl) {
            timerEl.textContent = UTILS.formatearTiempo(segundos);
            
            if (segundos <= 10) {
                timerEl.style.color = '#f5576c';
            }
        }
        
        if (segundos <= 0) {
            clearInterval(timerInterval);
            responderPregunta(''); // Pasar sin responder
        }
    }, 1000);
}

/**
 * Finalizar quiz
 */
function finalizarQuiz() {
    if (timerInterval) {
        clearInterval(timerInterval);
    }
    
    const correctas = quizActual.respuestas.filter(r => r.correcta).length;
    const total = quizActual.respuestas.length;
    const porcentaje = UTILS.calcularPorcentaje(correctas, total);
    
    const resultado = {
        modo: quizActual.modo,
        correctas,
        total,
        porcentaje,
        puntos: quizActual.puntos,
        racha: quizActual.racha,
        tiempo: Date.now() - quizActual.tiempoInicio
    };
    
    mostrarResultados(resultado);
}

/**
 * Finalizar quiz Pesadilla (por error)
 */
function finalizarQuizPesadilla() {
    UNIPAZ.mostrarNotificacion('💀 Modo Pesadilla: ¡Cometiste un error! Game Over.', 'error');
    setTimeout(() => {
        finalizarQuiz();
    }, 2000);
}

/**
 * Mostrar resultados
 */
function mostrarResultados(resultado) {
    const contenedor = document.getElementById('resultadoContainer');
    if (!contenedor) return;
    
    const icon = resultado.porcentaje >= 80 ? '🎉' : resultado.porcentaje >= 60 ? '✨' : '📚';
    
    let html = `
        <div class="resultado-card">
            <div class="resultado-icon">${icon}</div>
            
            <h2>Quiz Completado</h2>
            
            <div class="resultado-stats">
                <div class="stat">
                    <span>Correctas</span>
                    <strong>${resultado.correctas}/${resultado.total}</strong>
                </div>
                <div class="stat">
                    <span>Porcentaje</span>
                    <strong>${resultado.porcentaje}%</strong>
                </div>
                <div class="stat">
                    <span>Puntos</span>
                    <strong>${resultado.puntos}</strong>
                </div>
            </div>
            
            <div class="resultado-acciones">
                <button class="btn" onclick="location.href='/materias'">Volver a Materias</button>
                <button class="btn btn-secondary" onclick="location.reload()">Intentar Otro Quiz</button>
            </div>
        </div>
    `;
    
    contenedor.innerHTML = html;
}

/**
 * Salir del quiz
 */
function salirQuiz() {
    if (confirm('¿Estás seguro? Se perderá tu progreso.')) {
        if (timerInterval) {
            clearInterval(timerInterval);
        }
        location.href = '/materias';
    }
}

// ===== INICIALIZACIÓN =====

document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ quiz.js inicializado');
    
    // Listeners para botones de modo
    document.querySelectorAll('[data-modo]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const modo = e.target.dataset.modo;
            const materiaId = new URLSearchParams(window.location.search).get('materia');
            iniciarQuiz(modo, materiaId);
        });
    });
});

// Exportar globalmente
window.QUIZ = {
    iniciarQuiz,
    cargarPreguntas,
    mostrarPregunta,
    responderPregunta,
    registrarRespuesta,
    iniciarTimer,
    finalizarQuiz,
    mostrarResultados,
    salirQuiz
};

console.log('✅ quiz.js listo para usar');