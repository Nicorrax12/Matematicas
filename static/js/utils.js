// utils.js - Utilidades Generales UNIPAZ

console.log('✅ utils.js cargado');

// ===== VALIDACIÓN =====

/**
 * Validar email
 */
function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

/**
 * Validar contraseña
 */
function validarContrasena(contrasena) {
    return contrasena.length >= 8;
}

/**
 * Validar respuesta de pregunta
 */
function validarRespuesta(respuesta) {
    return respuesta && respuesta.trim().length > 0;
}

// ===== MANIPULACIÓN DOM =====

/**
 * Crear elemento HTML
 */
function crearElemento(tag, opciones = {}) {
    const elemento = document.createElement(tag);
    
    if (opciones.clase) {
        elemento.className = opciones.clase;
    }
    if (opciones.id) {
        elemento.id = opciones.id;
    }
    if (opciones.html) {
        elemento.innerHTML = opciones.html;
    }
    if (opciones.texto) {
        elemento.textContent = opciones.texto;
    }
    if (opciones.atributos) {
        Object.entries(opciones.atributos).forEach(([key, value]) => {
            elemento.setAttribute(key, value);
        });
    }
    if (opciones.estilos) {
        Object.assign(elemento.style, opciones.estilos);
    }
    
    return elemento;
}

/**
 * Agregar múltiples clases
 */
function agregarClases(elemento, clases) {
    if (typeof clases === 'string') {
        elemento.classList.add(clases);
    } else if (Array.isArray(clases)) {
        clases.forEach(clase => elemento.classList.add(clase));
    }
}

/**
 * Remover múltiples clases
 */
function removerClases(elemento, clases) {
    if (typeof clases === 'string') {
        elemento.classList.remove(clases);
    } else if (Array.isArray(clases)) {
        clases.forEach(clase => elemento.classList.remove(clase));
    }
}

/**
 * Toggle clase
 */
function toggleClase(elemento, clase) {
    elemento.classList.toggle(clase);
}

/**
 * Mostrar elemento
 */
function mostrarElemento(elemento, tipo = 'block') {
    elemento.style.display = tipo;
}

/**
 * Ocultar elemento
 */
function ocultarElemento(elemento) {
    elemento.style.display = 'none';
}

// ===== OPERACIONES CON ARRAYS =====

/**
 * Agrupar array por propiedad
 */
function agruparPor(array, propiedad) {
    return array.reduce((grupos, item) => {
        const clave = item[propiedad];
        if (!grupos[clave]) {
            grupos[clave] = [];
        }
        grupos[clave].push(item);
        return grupos;
    }, {});
}

/**
 * Filtrar array por propiedad
 */
function filtrarPor(array, propiedad, valor) {
    return array.filter(item => item[propiedad] === valor);
}

/**
 * Encontrar elemento por propiedad
 */
function encontrarPor(array, propiedad, valor) {
    return array.find(item => item[propiedad] === valor);
}

/**
 * Ordenar array por propiedad
 */
function ordenarPor(array, propiedad, ascendente = true) {
    const copia = [...array];
    return copia.sort((a, b) => {
        if (ascendente) {
            return a[propiedad] > b[propiedad] ? 1 : -1;
        } else {
            return a[propiedad] < b[propiedad] ? 1 : -1;
        }
    });
}

/**
 * Mapear array
 */
function mapear(array, propiedad) {
    return array.map(item => item[propiedad]);
}

// ===== OPERACIONES CON OBJETOS =====

/**
 * Combinar objetos
 */
function combinarObjetos(...objetos) {
    return Object.assign({}, ...objetos);
}

/**
 * Clonar objeto profundamente
 */
function clonarObjeto(obj) {
    return JSON.parse(JSON.stringify(obj));
}

/**
 * Obtener keys del objeto
 */
function obtenerKeys(obj) {
    return Object.keys(obj);
}

/**
 * Obtener values del objeto
 */
function obtenerValues(obj) {
    return Object.values(obj);
}

// ===== OPERACIONES CON NÚMEROS =====

/**
 * Generar número aleatorio
 */
function numeroAleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Redondear a decimales
 */
function redondear(numero, decimales) {
    return Math.round(numero * Math.pow(10, decimales)) / Math.pow(10, decimales);
}

/**
 * Calcular porcentaje
 */
function calcularPorcentaje(parte, total) {
    return redondear((parte / total) * 100, 2);
}

/**
 * Calcular promedio
 */
function calcularPromedio(numeros) {
    return numeros.reduce((a, b) => a + b, 0) / numeros.length;
}

/**
 * Sumar array
 */
function sumarArray(numeros) {
    return numeros.reduce((a, b) => a + b, 0);
}

// ===== OPERACIONES CON STRINGS =====

/**
 * Capitalizar string
 */
function capitalizar(texto) {
    return texto.charAt(0).toUpperCase() + texto.slice(1);
}

/**
 * Convertir a mayúsculas
 */
function aMayusculas(texto) {
    return texto.toUpperCase();
}

/**
 * Convertir a minúsculas
 */
function aMinusculas(texto) {
    return texto.toLowerCase();
}

/**
 * Invertir string
 */
function invertirString(texto) {
    return texto.split('').reverse().join('');
}

/**
 * Eliminar espacios
 */
function eliminarEspacios(texto) {
    return texto.replace(/\s/g, '');
}

/**
 * Truncar texto
 */
function truncarTexto(texto, longitud) {
    return texto.length > longitud ? texto.substring(0, longitud) + '...' : texto;
}

/**
 * Contar palabras
 */
function contarPalabras(texto) {
    return texto.split(/\s+/).filter(word => word.length > 0).length;
}

// ===== TIEMPO =====

/**
 * Obtener hora actual
 */
function obtenerHoraActual() {
    return new Date().toLocaleTimeString('es-CO');
}

/**
 * Obtener fecha actual
 */
function obtenerFechaActual() {
    return new Date().toLocaleDateString('es-CO');
}

/**
 * Calcular diferencia de fechas
 */
function diferenciaDias(fecha1, fecha2) {
    const d1 = new Date(fecha1);
    const d2 = new Date(fecha2);
    const diferencia = Math.abs(d2 - d1);
    return Math.ceil(diferencia / (1000 * 60 * 60 * 24));
}

/**
 * Formatear tiempo en MM:SS
 */
function formatearTiempo(segundos) {
    const minutos = Math.floor(segundos / 60);
    const segs = segundos % 60;
    return `${minutos.toString().padStart(2, '0')}:${segs.toString().padStart(2, '0')}`;
}

/**
 * Cuenta regresiva
 */
function cuentaRegresiva(segundos, callback) {
    let tiempoRestante = segundos;
    
    const intervalo = setInterval(() => {
        tiempoRestante--;
        
        if (callback) {
            callback(tiempoRestante);
        }
        
        if (tiempoRestante <= 0) {
            clearInterval(intervalo);
        }
    }, 1000);
    
    return intervalo;
}

// ===== EVENTOS =====

/**
 * Esperar a que se cargue elemento
 */
function esperarElemento(selector) {
    return new Promise(resolve => {
        const elemento = document.querySelector(selector);
        if (elemento) {
            resolve(elemento);
        } else {
            const observer = new MutationObserver(() => {
                const elem = document.querySelector(selector);
                if (elem) {
                    observer.disconnect();
                    resolve(elem);
                }
            });
            observer.observe(document.body, { childList: true, subtree: true });
        }
    });
}

/**
 * Debounce para funciones
 */
function debounce(funcion, espera) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => funcion.apply(this, args), espera);
    };
}

/**
 * Throttle para funciones
 */
function throttle(funcion, limite) {
    let ultima = 0;
    return function(...args) {
        const ahora = Date.now();
        if (ahora - ultima > limite) {
            funcion.apply(this, args);
            ultima = ahora;
        }
    };
}

// ===== UTILIDADES GENERALES =====

/**
 * Copiar al portapapeles
 */
function copiarAlPortapapeles(texto) {
    navigator.clipboard.writeText(texto).then(() => {
        console.log('Copiado al portapapeles:', texto);
    });
}

/**
 * Descargar archivo
 */
function descargarArchivo(datos, nombre, tipo = 'application/json') {
    const blob = new Blob([datos], { type: tipo });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = nombre;
    a.click();
    window.URL.revokeObjectURL(url);
}

/**
 * Esperar X milisegundos
 */
function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Ejecutar en paralelo
 */
async function enParalelo(promesas) {
    return Promise.all(promesas);
}

/**
 * Ejecutar en secuencia
 */
async function enSecuencia(promesas) {
    const resultados = [];
    for (const promesa of promesas) {
        resultados.push(await promesa);
    }
    return resultados;
}

// Exportar globalmente
window.UTILS = {
    validarEmail,
    validarContrasena,
    validarRespuesta,
    crearElemento,
    agregarClases,
    removerClases,
    toggleClase,
    mostrarElemento,
    ocultarElemento,
    agruparPor,
    filtrarPor,
    encontrarPor,
    ordenarPor,
    mapear,
    combinarObjetos,
    clonarObjeto,
    obtenerKeys,
    obtenerValues,
    numeroAleatorio,
    redondear,
    calcularPorcentaje,
    calcularPromedio,
    sumarArray,
    capitalizar,
    aMayusculas,
    aMinusculas,
    invertirString,
    eliminarEspacios,
    truncarTexto,
    contarPalabras,
    obtenerHoraActual,
    obtenerFechaActual,
    diferenciaDias,
    formatearTiempo,
    cuentaRegresiva,
    esperarElemento,
    debounce,
    throttle,
    copiarAlPortapapeles,
    descargarArchivo,
    esperar,
    enParalelo,
    enSecuencia
};

console.log('✅ utils.js listo para usar');