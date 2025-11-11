// notifications.js - Sistema de notificaciones en tiempo real

console.log('✅ notifications.js cargado');

class NotificationManager {
    constructor() {
        this.notificaciones = [];
        this.queue = [];
        this.isProcessing = false;
    }

    /**
     * Crear notificación
     */
    crear(titulo, mensaje, tipo = 'info', duracion = 3000) {
        const id = Date.now();
        const notif = {
            id,
            titulo,
            mensaje,
            tipo,
            duracion,
            timestamp: new Date()
        };

        this.notificaciones.push(notif);
        this.mostrar(notif);

        if (duracion > 0) {
            setTimeout(() => this.cerrar(id), duracion);
        }

        return id;
    }

    /**
     * Mostrar notificación en pantalla
     */
    mostrar(notif) {
        const container = this.obtenerContenedor();
        
        const html = `
            <div class="notificacion notif-${notif.tipo}" id="notif_${notif.id}">
                <div class="notif-header">
                    <h4>${notif.titulo}</h4>
                    <button onclick="NOTIFICATIONS.cerrar(${notif.id})">✕</button>
                </div>
                <p>${notif.mensaje}</p>
            </div>
        `;

        const el = document.createElement('div');
        el.innerHTML = html;
        container.appendChild(el.firstElementChild);

        // Animación de entrada
        requestAnimationFrame(() => {
            document.getElementById(`notif_${notif.id}`)?.classList.add('show');
        });
    }

    /**
     * Cerrar notificación
     */
    cerrar(id) {
        const el = document.getElementById(`notif_${id}`);
        if (el) {
            el.classList.remove('show');
            setTimeout(() => el.remove(), 300);
        }

        this.notificaciones = this.notificaciones.filter(n => n.id !== id);
    }

    /**
     * Obtener contenedor
     */
    obtenerContenedor() {
        let container = document.getElementById('notificationsContainer');
        if (!container) {
            container = document.createElement('div');
            container.id = 'notificationsContainer';
            container.className = 'notifications-container';
            document.body.appendChild(container);
        }
        return container;
    }

    /**
     * Éxito
     */
    exito(titulo, mensaje = '', duracion = 3000) {
        return this.crear(titulo, mensaje, 'success', duracion);
    }

    /**
     * Error
     */
    error(titulo, mensaje = '', duracion = 5000) {
        return this.crear(titulo, mensaje, 'error', duracion);
    }

    /**
     * Advertencia
     */
    advertencia(titulo, mensaje = '', duracion = 4000) {
        return this.crear(titulo, mensaje, 'warning', duracion);
    }

    /**
     * Info
     */
    info(titulo, mensaje = '', duracion = 3000) {
        return this.crear(titulo, mensaje, 'info', duracion);
    }

    /**
     * Confirmar acción
     */
    confirmar(titulo, mensaje, onConfirm, onCancel) {
        const id = Date.now();
        const container = this.obtenerContenedor();

        const html = `
            <div class="notificacion notif-confirmar" id="notif_${id}">
                <h4>${titulo}</h4>
                <p>${mensaje}</p>
                <div class="notif-acciones">
                    <button class="btn btn-confirm" onclick="NOTIFICATIONS.procesarConfirmacion(${id}, true)">
                        Confirmar
                    </button>
                    <button class="btn btn-cancel" onclick="NOTIFICATIONS.procesarConfirmacion(${id}, false)">
                        Cancelar
                    </button>
                </div>
            </div>
        `;

        const el = document.createElement('div');
        el.innerHTML = html;
        container.appendChild(el.firstElementChild);

        this.notificaciones.push({
            id,
            titulo,
            tipo: 'confirmar',
            onConfirm,
            onCancel
        });
    }

    /**
     * Procesar confirmación
     */
    procesarConfirmacion(id, confirmado) {
        const notif = this.notificaciones.find(n => n.id === id);
        if (notif) {
            if (confirmado && notif.onConfirm) {
                notif.onConfirm();
            } else if (!confirmado && notif.onCancel) {
                notif.onCancel();
            }
            this.cerrar(id);
        }
    }

    /**
     * Toast (notificación rápida)
     */
    toast(mensaje, tipo = 'info') {
        this.crear('', mensaje, tipo, 2000);
    }
}

// Crear instancia global
window.NOTIFICATIONS = new NotificationManager();

console.log('✅ notifications.js listo');