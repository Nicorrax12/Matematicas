/* ========== MATH PANEL WIDGET - JavaScript FINAL CORREGIDO ========== */

class MathPanelWidget {
    constructor() {
        this.currentTab = 'calculus';
        this.activeElement = null;
        this.isDragging = false;
        this.dragOffsetX = 0;
        this.dragOffsetY = 0;

        // Fórmulas organizadas por categoría
        this.formulas = {
            calculus: [
                { symbol: '∫', latex: '\\int' },
                { symbol: '∂', latex: '\\partial' },
                { symbol: '∑', latex: '\\sum' },
                { symbol: 'lim', latex: '\\lim_{x \\to a}' },
                { symbol: 'dy/dx', latex: '\\frac{d}{dx}' },
                { symbol: '∫ᵃᵇ', latex: '\\int_{a}^{b}' },
            ],
            algebra: [
                { symbol: 'x²', latex: '^{2}' },
                { symbol: 'xⁿ', latex: '^{n}' },
                { symbol: '√', latex: '\\sqrt{x}' },
                { symbol: '√ⁿ', latex: '\\sqrt[n]{x}' },
                { symbol: 'a/b', latex: '\\frac{a}{b}' },
                { symbol: 'xᵢ', latex: '_{i}' },
            ],
            functions: [
                { symbol: 'sin', latex: '\\sin' },
                { symbol: 'cos', latex: '\\cos' },
                { symbol: 'tan', latex: '\\tan' },
                { symbol: 'log', latex: '\\log' },
                { symbol: 'ln', latex: '\\ln' },
                { symbol: 'eˣ', latex: 'e^{x}' },
            ],
            symbols: [
                { symbol: '∞', latex: '\\infty' },
                { symbol: '≤', latex: '\\leq' },
                { symbol: '≥', latex: '\\geq' },
                { symbol: '≠', latex: '\\neq' },
                { symbol: '±', latex: '\\pm' },
                { symbol: '≈', latex: '\\approx' },
            ],
            greek: [
                { symbol: 'α', latex: '\\alpha' },
                { symbol: 'β', latex: '\\beta' },
                { symbol: 'γ', latex: '\\gamma' },
                { symbol: 'δ', latex: '\\delta' },
                { symbol: 'π', latex: '\\pi' },
                { symbol: 'θ', latex: '\\theta' },
            ],
            logic: [
                { symbol: '∧', latex: '\\wedge' },
                { symbol: '∨', latex: '\\vee' },
                { symbol: '¬', latex: '\\neg' },
                { symbol: '∀', latex: '\\forall' },
                { symbol: '∃', latex: '\\exists' },
                { symbol: '→', latex: '\\rightarrow' },
            ],
        };

        this.init();
    }

    init() {
        console.log('🔧 Inicializando MathPanelWidget...');
        this.createHTML();
        this.attachEventListeners();
        this.trackActiveElement();
        console.log('✓ MathPanelWidget listo');
    }

    createHTML() {
        const widget = document.createElement('div');
        widget.className = 'math-panel-widget';
        widget.id = 'mathPanelWidget';

        // Botón flotante
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'math-panel-toggle';
        toggleBtn.textContent = '∑ₓ';
        toggleBtn.id = 'mathToggleBtn';
        toggleBtn.title = 'Panel de fórmulas matemáticas';
        toggleBtn.type = 'button';
        toggleBtn.onclick = (e) => {
            e.preventDefault();
            e.stopPropagation();
            this.toggle();
        };

        // Panel contenedor
        const container = document.createElement('div');
        container.className = 'math-panel-container';
        container.id = 'mathPanelContainer';

        // Header
        const header = document.createElement('div');
        header.className = 'math-panel-header';
        header.innerHTML = `
            <h3>📐 Fórmulas Matemáticas</h3>
            <button class="math-panel-close" id="mathCloseBtn" type="button">✕</button>
        `;

        // Tabs
        const tabs = document.createElement('div');
        tabs.className = 'math-panel-tabs';
        tabs.id = 'mathTabs';
        
        const tabNames = {
            calculus: 'Cálculo',
            algebra: 'Álgebra',
            functions: 'Funciones',
            symbols: 'Símbolos',
            greek: 'Griego',
            logic: 'Lógica'
        };

        Object.keys(tabNames).forEach((key, idx) => {
            const btn = document.createElement('button');
            btn.className = `math-panel-tab ${idx === 0 ? 'active' : ''}`;
            btn.textContent = tabNames[key];
            btn.type = 'button';
            btn.onclick = (e) => {
                e.preventDefault();
                e.stopPropagation();
                this.switchTab(key);
            };
            btn.dataset.tab = key;
            tabs.appendChild(btn);
        });

        // Contenido
        const content = document.createElement('div');
        content.className = 'math-panel-content';
        content.id = 'mathPanelContent';

        // Agregar todo
        container.appendChild(header);
        container.appendChild(tabs);
        container.appendChild(content);

        widget.appendChild(toggleBtn);
        widget.appendChild(container);

        document.body.appendChild(widget);

        // Renderizar fórmulas iniciales
        this.renderFormulas('calculus');

        // Hacer el header draggable
        this.makeDraggable(header, container);
    }

    renderFormulas(category) {
        console.log('🎨 Renderizando fórmulas de:', category);
        const container = document.getElementById('mathPanelContent');
        container.innerHTML = '';
        
        const formulas = this.formulas[category] || [];
        console.log('📊 Fórmulas disponibles:', formulas.length);

        if (formulas.length === 0) {
            container.innerHTML = '<div class="math-panel-empty">No hay fórmulas</div>';
            return;
        }

        formulas.forEach((f) => {
            const btn = document.createElement('button');
            btn.className = 'math-key';
            btn.type = 'button';
            btn.innerHTML = `<span>${f.symbol}</span>`;
            btn.title = f.latex;
            btn.onclick = (e) => {
                e.preventDefault();
                e.stopPropagation();
                this.insertFormula(f.latex);
                return false;
            };
            container.appendChild(btn);
        });

        console.log('✓ Fórmulas renderizadas');
    }

    switchTab(tabName) {
        console.log('🔄 Cambiando a tab:', tabName);

        // Actualizar botones activos
        document.querySelectorAll('.math-panel-tab').forEach(btn => {
            btn.classList.remove('active');
        });
        
        const activeTab = document.querySelector(`[data-tab="${tabName}"]`);
        if (activeTab) {
            activeTab.classList.add('active');
            console.log('✓ Tab activo:', tabName);
        }

        // Actualizar contenido
        this.currentTab = tabName;
        this.renderFormulas(tabName);
    }

    insertFormula(latex) {
        console.log('📝 Insertando fórmula:', latex);
        console.log('📍 Elemento activo:', this.activeElement);

        if (!this.activeElement) {
            console.warn('⚠️ No hay elemento activo');
            this.showNotification('❌ Haz click en un campo primero', true);
            return;
        }

        try {
            // Verificar que el elemento sea contenteditable
            if (this.activeElement.contentEditable !== 'true') {
                console.warn('⚠️ Elemento no es contenteditable');
                this.showNotification('❌ El campo no es editable', true);
                return;
            }

            // Obtener la selección actual
            const selection = window.getSelection();
            const range = selection.rangeCount > 0 ? selection.getRangeAt(0) : null;

            // Crear un nodo de texto con la fórmula
            const formulaNode = document.createTextNode(latex);

            if (range) {
                // Si hay selección, reemplazarla
                range.deleteContents();
                range.insertNode(formulaNode);
                // Mover el cursor después de la fórmula
                range.setStartAfter(formulaNode);
                range.collapse(true);
                selection.removeAllRanges();
                selection.addRange(range);
            } else {
                // Si no hay selección, insertar al final
                this.activeElement.appendChild(formulaNode);
            }

            // Hacer focus en el elemento
            this.activeElement.focus();

            // Renderizar MathJax
            if (window.MathJax) {
                console.log('🎨 Renderizando MathJax...');
                MathJax.typesetPromise([this.activeElement]).catch(err => console.log('MathJax error:', err));
            }

            console.log('✓ Fórmula insertada');
            this.showNotification('✓ Fórmula insertada', false);
        } catch (e) {
            console.error('❌ Error insertando fórmula:', e);
            this.showNotification('❌ Error al insertar fórmula', true);
        }
    }

    toggle() {
        console.log('🔘 Toggle panel');
        const container = document.getElementById('mathPanelContainer');
        const toggleBtn = document.getElementById('mathToggleBtn');

        container.classList.toggle('expanded');
        toggleBtn.classList.toggle('expanded');

        console.log('Estado expanded:', container.classList.contains('expanded'));
    }

    attachEventListeners() {
        const closeBtn = document.getElementById('mathCloseBtn');
        if (closeBtn) {
            closeBtn.onclick = (e) => {
                e.preventDefault();
                e.stopPropagation();
                this.toggle();
                return false;
            };
        }
    }

    trackActiveElement() {
        // Usar focusin para contenteditable y textarea/input
        document.addEventListener('focusin', (e) => {
            if (e.target.contentEditable === 'true' || 
                e.target.tagName === 'TEXTAREA' || 
                e.target.tagName === 'INPUT') {
                this.activeElement = e.target;
                console.log('✓ Elemento activo:', e.target.id || e.target.className);
            }
        });

        // También hacer click en contenteditable lo selecciona
        document.addEventListener('click', (e) => {
            if (e.target.contentEditable === 'true') {
                this.activeElement = e.target;
                console.log('✓ Click en contenteditable:', e.target.id);
            }
        }, true);
    }

    makeDraggable(header, container) {
        let isDragging = false;
        let offsetX = 0;
        let offsetY = 0;

        header.addEventListener('mousedown', (e) => {
            isDragging = true;
            const rect = container.getBoundingClientRect();
            offsetX = e.clientX - rect.left;
            offsetY = e.clientY - rect.top;
            console.log('🖱️ Dragging iniciado');
        });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;

            const x = e.clientX - offsetX;
            const y = e.clientY - offsetY;

            container.style.bottom = 'auto';
            container.style.right = 'auto';
            container.style.left = Math.max(0, x) + 'px';
            container.style.top = Math.max(0, y) + 'px';
        });

        document.addEventListener('mouseup', () => {
            if (isDragging) {
                console.log('✓ Dragging finalizado');
            }
            isDragging = false;
        });
    }

    showNotification(msg, isError = false) {
        const div = document.createElement('div');
        div.className = `notification ${isError ? 'error' : ''}`;
        div.textContent = msg;
        div.style.cssText = `
            position: fixed;
            bottom: 100px;
            right: 30px;
            padding: 1rem 1.5rem;
            background: ${isError ? 'rgba(244, 67, 54, 0.9)' : 'rgba(0, 150, 136, 0.9)'};
            color: white;
            border-radius: 6px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
            animation: slideUp 0.3s ease;
            z-index: 9999;
        `;
        document.body.appendChild(div);
        setTimeout(() => {
            div.style.animation = 'slideDown 0.3s ease';
            setTimeout(() => div.remove(), 300);
        }, 2000);
    }
}

// Inicializar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        console.log('📍 DOMContentLoaded - Iniciando MathPanel');
        window.mathPanel = new MathPanelWidget();
    });
} else {
    console.log('📍 DOM ya cargado - Iniciando MathPanel');
    window.mathPanel = new MathPanelWidget();
}