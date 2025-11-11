# Documentación Completa del Proyecto para IA
============================================================

**Generado:** 2025-11-10 21:53:24
**Ruta del proyecto:** C:\xampp\htdocs\proyecto


## 📊 RESUMEN DEL PROYECTO
------------------------------------------------------------
- **Total de archivos procesados:** 67
- **Total de líneas de código:** 18,836
- **Archivos Python:** 15
- **Archivos JavaScript:** 15
- **Archivos HTML:** 15
- **Archivos CSS:** 4
- **Otros archivos:** 18


## 📁 ESTRUCTURA DEL PROYECTO
------------------------------------------------------------
```
proyecto/
  README.md
  app.py
  env
  export_routes.py
  init_db.py
  mega_generador_unipaz.py
  requirements.txt
  rutas.json
  rutas.txt
  rutas_y_redirecciones.json
  rutas_y_redirecciones.txt
  backend/
    routes.py
    config/
    models/
      __init__.py
      concurso.py
      ranking.py
      usuario.py
    services/
      __init__.py
      concurso_service.py
      ranking_service.py
  database/
    schema.sql
    seeds.sql
    migrations/
      001_initial.sql
      002_add_rankings.sql
  docs/
    API.md
    DATABASE.md
    SETUP.md
  static/
    css/
      animations.css
      math-panel.css
      responsive.css
      style.css
    data/
      carreras.json
      config.json
      logros.json
      materias.json
    images/
      logo.png
      avatars/
    js/
      analytics.js
      api-config.js
      auth.js
      concursos.js
      export-data.js
      localStorage-helper.js
      logros.js
      main.js
      materias.js
      math-panel.js
      notifications.js
      quiz.js
      ranking.js
      search.js
      utils.js
  templates/
    admin_panel.html
    concursos.html
    crear-examen.html
    dashboard.html
    debug-examen.html
    duelo.html
    index.html
    login.html
    logros.html
    materias.html
    perfil.html
    quiz.html
    rankings.html
    registro.html
    unirse-examen.html
  tests/
    __init__.py
    test_concursos.py
    test_rankings.py
```


## 📄 CONTENIDO DETALLADO DE ARCHIVOS
------------------------------------------------------------


### CSS (4 archivos)

#### `static\css\animations.css`
- **Líneas:** 1402
- **Tamaño:** 35874 bytes

**Contenido:**
```css
:root {
  /* Primitive Color Tokens */
  --color-white: rgba(255, 255, 255, 1);
  --color-black: rgba(0, 0, 0, 1);
  --color-cream-50: rgba(252, 252, 249, 1);
  --color-cream-100: rgba(255, 255, 253, 1);
  --color-gray-200: rgba(245, 245, 245, 1);
  --color-gray-300: rgba(167, 169, 169, 1);
  --color-gray-400: rgba(119, 124, 124, 1);
  --color-slate-500: rgba(98, 108, 113, 1);
  --color-brown-600: rgba(94, 82, 64, 1);
  --color-charcoal-700: rgba(31, 33, 33, 1);
  --color-charcoal-800: rgba(38, 40, 40, 1);
  --color-slate-900: rgba(19, 52, 59, 1);
  --color-teal-300: rgba(50, 184, 198, 1);
  --color-teal-400: rgba(45, 166, 178, 1);
  --color-teal-500: rgba(33, 128, 141, 1);
  --color-teal-600: rgba(29, 116, 128, 1);
  --color-teal-700: rgba(26, 104, 115, 1);
  --color-teal-800: rgba(41, 150, 161, 1);
  --color-red-400: rgba(255, 84, 89, 1);
  --color-red-500: rgba(192, 21, 47, 1);
  --color-orange-400: rgba(230, 129, 97, 1);
  --color-orange-500: rgba(168, 75, 47, 1);

  /* RGB versions for opacity control */
  --color-brown-600-rgb: 94, 82, 64;
  --color-teal-500-rgb: 33, 128, 141;
  --color-slate-900-rgb: 19, 52, 59;
  --color-slate-500-rgb: 98, 108, 113;
  --color-red-500-rgb: 192, 21, 47;
  --color-red-400-rgb: 255, 84, 89;
  --color-orange-500-rgb: 168, 75, 47;
  --color-orange-400-rgb: 230, 129, 97;

  /* Background color tokens (Light Mode) */
  --color-bg-1: rgba(59, 130, 246, 0.08); /* Light blue */
  --color-bg-2: rgba(245, 158, 11, 0.08); /* Light yellow */
  --color-bg-3: rgba(34, 197, 94, 0.08); /* Light green */
  --color-bg-4: rgba(239, 68, 68, 0.08); /* Light red */
  --color-bg-5: rgba(147, 51, 234, 0.08); /* Light purple */
  --color-bg-6: rgba(249, 115, 22, 0.08); /* Light orange */
  --color-bg-7: rgba(236, 72, 153, 0.08); /* Light pink */
  --color-bg-8: rgba(6, 182, 212, 0.08); /* Light cyan */

  /* Semantic Color Tokens (Light Mode) */
  --color-background: var(--color-cream-50);
  --color-surface: var(--color-cream-100);
  --color-text: var(--color-slate-900);
  --color-text-secondary: var(--color-slate-500);
  --color-primary: var(--color-teal-500);
  --color-primary-hover: var(--color-teal-600);
  --color-primary-active: var(--color-teal-700);
  --color-secondary: rgba(var(--color-brown-600-rgb), 0.12);
  --color-secondary-hover: rgba(var(--color-brown-600-rgb), 0.2);
  --color-secondary-active: rgba(var(--color-brown-600-rgb), 0.25);
  --color-border: rgba(var(--color-brown-600-rgb), 0.2);
  --color-btn-primary-text: var(--color-cream-50);
  --color-card-border: rgba(var(--color-brown-600-rgb), 0.12);
  --color-card-border-inner: rgba(var(--color-brown-600-rgb), 0.12);
  --color-error: var(--color-red-500);
  --color-success: var(--color-teal-500);
  --color-warning: var(--color-orange-500);
  --color-info: var(--color-slate-500);
  --color-focus-ring: rgba(var(--color-teal-500-rgb), 0.4);
  --color-select-caret: rgba(var(--color-slate-900-rgb), 0.8);

  /* Common style patterns */
  --focus-ring: 0 0 0 3px var(--color-focus-ring);
  --focus-outline: 2px solid var(--color-primary);
  --status-bg-opacity: 0.15;
  --status-border-opacity: 0.25;
  --select-caret-light: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23134252' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --select-caret-dark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23f5f5f5' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");

  /* RGB versions for opacity control */
  --color-success-rgb: 33, 128, 141;
  --color-error-rgb: 192, 21, 47;
  --color-warning-rgb: 168, 75, 47;
  --color-info-rgb: 98, 108, 113;

  /* Typography */
  --font-family-base: "FKGroteskNeue", "Geist", "Inter", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-family-mono: "Berkeley Mono", ui-monospace, SFMono-Regular, Menlo,
    Monaco, Consolas, monospace;
  --font-size-xs: 11px;
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-md: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 18px;
  --font-size-2xl: 20px;
  --font-size-3xl: 24px;
  --font-size-4xl: 30px;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 550;
  --font-weight-bold: 600;
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;
  --letter-spacing-tight: -0.01em;

  /* Spacing */
  --space-0: 0;
  --space-1: 1px;
  --space-2: 2px;
  --space-4: 4px;
  --space-6: 6px;
  --space-8: 8px;
  --space-10: 10px;
  --space-12: 12px;
  --space-16: 16px;
  --space-20: 20px;
  --space-24: 24px;
  --space-32: 32px;

  /* Border Radius */
  --radius-sm: 6px;
  --radius-base: 8px;
  --radius-md: 10px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-xs: 0 1p
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\css\math-panel.css`
- **Líneas:** 1121
- **Tamaño:** 31760 bytes

**Contenido:**
```css
:root {
  /* Primitive Color Tokens */
  --color-white: rgba(255, 255, 255, 1);
  --color-black: rgba(0, 0, 0, 1);
  --color-cream-50: rgba(252, 252, 249, 1);
  --color-cream-100: rgba(255, 255, 253, 1);
  --color-gray-200: rgba(245, 245, 245, 1);
  --color-gray-300: rgba(167, 169, 169, 1);
  --color-gray-400: rgba(119, 124, 124, 1);
  --color-slate-500: rgba(98, 108, 113, 1);
  --color-brown-600: rgba(94, 82, 64, 1);
  --color-charcoal-700: rgba(31, 33, 33, 1);
  --color-charcoal-800: rgba(38, 40, 40, 1);
  --color-slate-900: rgba(19, 52, 59, 1);
  --color-teal-300: rgba(50, 184, 198, 1);
  --color-teal-400: rgba(45, 166, 178, 1);
  --color-teal-500: rgba(33, 128, 141, 1);
  --color-teal-600: rgba(29, 116, 128, 1);
  --color-teal-700: rgba(26, 104, 115, 1);
  --color-teal-800: rgba(41, 150, 161, 1);
  --color-red-400: rgba(255, 84, 89, 1);
  --color-red-500: rgba(192, 21, 47, 1);
  --color-orange-400: rgba(230, 129, 97, 1);
  --color-orange-500: rgba(168, 75, 47, 1);

  /* RGB versions for opacity control */
  --color-brown-600-rgb: 94, 82, 64;
  --color-teal-500-rgb: 33, 128, 141;
  --color-slate-900-rgb: 19, 52, 59;
  --color-slate-500-rgb: 98, 108, 113;
  --color-red-500-rgb: 192, 21, 47;
  --color-red-400-rgb: 255, 84, 89;
  --color-orange-500-rgb: 168, 75, 47;
  --color-orange-400-rgb: 230, 129, 97;

  /* Background color tokens (Light Mode) */
  --color-bg-1: rgba(59, 130, 246, 0.08); /* Light blue */
  --color-bg-2: rgba(245, 158, 11, 0.08); /* Light yellow */
  --color-bg-3: rgba(34, 197, 94, 0.08); /* Light green */
  --color-bg-4: rgba(239, 68, 68, 0.08); /* Light red */
  --color-bg-5: rgba(147, 51, 234, 0.08); /* Light purple */
  --color-bg-6: rgba(249, 115, 22, 0.08); /* Light orange */
  --color-bg-7: rgba(236, 72, 153, 0.08); /* Light pink */
  --color-bg-8: rgba(6, 182, 212, 0.08); /* Light cyan */

  /* Semantic Color Tokens (Light Mode) */
  --color-background: var(--color-cream-50);
  --color-surface: var(--color-cream-100);
  --color-text: var(--color-slate-900);
  --color-text-secondary: var(--color-slate-500);
  --color-primary: var(--color-teal-500);
  --color-primary-hover: var(--color-teal-600);
  --color-primary-active: var(--color-teal-700);
  --color-secondary: rgba(var(--color-brown-600-rgb), 0.12);
  --color-secondary-hover: rgba(var(--color-brown-600-rgb), 0.2);
  --color-secondary-active: rgba(var(--color-brown-600-rgb), 0.25);
  --color-border: rgba(var(--color-brown-600-rgb), 0.2);
  --color-btn-primary-text: var(--color-cream-50);
  --color-card-border: rgba(var(--color-brown-600-rgb), 0.12);
  --color-card-border-inner: rgba(var(--color-brown-600-rgb), 0.12);
  --color-error: var(--color-red-500);
  --color-success: var(--color-teal-500);
  --color-warning: var(--color-orange-500);
  --color-info: var(--color-slate-500);
  --color-focus-ring: rgba(var(--color-teal-500-rgb), 0.4);
  --color-select-caret: rgba(var(--color-slate-900-rgb), 0.8);

  /* Common style patterns */
  --focus-ring: 0 0 0 3px var(--color-focus-ring);
  --focus-outline: 2px solid var(--color-primary);
  --status-bg-opacity: 0.15;
  --status-border-opacity: 0.25;
  --select-caret-light: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23134252' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --select-caret-dark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23f5f5f5' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");

  /* RGB versions for opacity control */
  --color-success-rgb: 33, 128, 141;
  --color-error-rgb: 192, 21, 47;
  --color-warning-rgb: 168, 75, 47;
  --color-info-rgb: 98, 108, 113;

  /* Typography */
  --font-family-base: "FKGroteskNeue", "Geist", "Inter", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-family-mono: "Berkeley Mono", ui-monospace, SFMono-Regular, Menlo,
    Monaco, Consolas, monospace;
  --font-size-xs: 11px;
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-md: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 18px;
  --font-size-2xl: 20px;
  --font-size-3xl: 24px;
  --font-size-4xl: 30px;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 550;
  --font-weight-bold: 600;
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;
  --letter-spacing-tight: -0.01em;

  /* Spacing */
  --space-0: 0;
  --space-1: 1px;
  --space-2: 2px;
  --space-4: 4px;
  --space-6: 6px;
  --space-8: 8px;
  --space-10: 10px;
  --space-12: 12px;
  --space-16: 16px;
  --space-20: 20px;
  --space-24: 24px;
  --space-32: 32px;

  /* Border Radius */
  --radius-sm: 6px;
  --radius-base: 8px;
  --radius-md: 10px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-xs: 0 1p
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\css\responsive.css`
- **Líneas:** 1272
- **Tamaño:** 34216 bytes

**Contenido:**
```css
:root {
  /* Primitive Color Tokens */
  --color-white: rgba(255, 255, 255, 1);
  --color-black: rgba(0, 0, 0, 1);
  --color-cream-50: rgba(252, 252, 249, 1);
  --color-cream-100: rgba(255, 255, 253, 1);
  --color-gray-200: rgba(245, 245, 245, 1);
  --color-gray-300: rgba(167, 169, 169, 1);
  --color-gray-400: rgba(119, 124, 124, 1);
  --color-slate-500: rgba(98, 108, 113, 1);
  --color-brown-600: rgba(94, 82, 64, 1);
  --color-charcoal-700: rgba(31, 33, 33, 1);
  --color-charcoal-800: rgba(38, 40, 40, 1);
  --color-slate-900: rgba(19, 52, 59, 1);
  --color-teal-300: rgba(50, 184, 198, 1);
  --color-teal-400: rgba(45, 166, 178, 1);
  --color-teal-500: rgba(33, 128, 141, 1);
  --color-teal-600: rgba(29, 116, 128, 1);
  --color-teal-700: rgba(26, 104, 115, 1);
  --color-teal-800: rgba(41, 150, 161, 1);
  --color-red-400: rgba(255, 84, 89, 1);
  --color-red-500: rgba(192, 21, 47, 1);
  --color-orange-400: rgba(230, 129, 97, 1);
  --color-orange-500: rgba(168, 75, 47, 1);

  /* RGB versions for opacity control */
  --color-brown-600-rgb: 94, 82, 64;
  --color-teal-500-rgb: 33, 128, 141;
  --color-slate-900-rgb: 19, 52, 59;
  --color-slate-500-rgb: 98, 108, 113;
  --color-red-500-rgb: 192, 21, 47;
  --color-red-400-rgb: 255, 84, 89;
  --color-orange-500-rgb: 168, 75, 47;
  --color-orange-400-rgb: 230, 129, 97;

  /* Background color tokens (Light Mode) */
  --color-bg-1: rgba(59, 130, 246, 0.08); /* Light blue */
  --color-bg-2: rgba(245, 158, 11, 0.08); /* Light yellow */
  --color-bg-3: rgba(34, 197, 94, 0.08); /* Light green */
  --color-bg-4: rgba(239, 68, 68, 0.08); /* Light red */
  --color-bg-5: rgba(147, 51, 234, 0.08); /* Light purple */
  --color-bg-6: rgba(249, 115, 22, 0.08); /* Light orange */
  --color-bg-7: rgba(236, 72, 153, 0.08); /* Light pink */
  --color-bg-8: rgba(6, 182, 212, 0.08); /* Light cyan */

  /* Semantic Color Tokens (Light Mode) */
  --color-background: var(--color-cream-50);
  --color-surface: var(--color-cream-100);
  --color-text: var(--color-slate-900);
  --color-text-secondary: var(--color-slate-500);
  --color-primary: var(--color-teal-500);
  --color-primary-hover: var(--color-teal-600);
  --color-primary-active: var(--color-teal-700);
  --color-secondary: rgba(var(--color-brown-600-rgb), 0.12);
  --color-secondary-hover: rgba(var(--color-brown-600-rgb), 0.2);
  --color-secondary-active: rgba(var(--color-brown-600-rgb), 0.25);
  --color-border: rgba(var(--color-brown-600-rgb), 0.2);
  --color-btn-primary-text: var(--color-cream-50);
  --color-card-border: rgba(var(--color-brown-600-rgb), 0.12);
  --color-card-border-inner: rgba(var(--color-brown-600-rgb), 0.12);
  --color-error: var(--color-red-500);
  --color-success: var(--color-teal-500);
  --color-warning: var(--color-orange-500);
  --color-info: var(--color-slate-500);
  --color-focus-ring: rgba(var(--color-teal-500-rgb), 0.4);
  --color-select-caret: rgba(var(--color-slate-900-rgb), 0.8);

  /* Common style patterns */
  --focus-ring: 0 0 0 3px var(--color-focus-ring);
  --focus-outline: 2px solid var(--color-primary);
  --status-bg-opacity: 0.15;
  --status-border-opacity: 0.25;
  --select-caret-light: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23134252' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --select-caret-dark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23f5f5f5' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");

  /* RGB versions for opacity control */
  --color-success-rgb: 33, 128, 141;
  --color-error-rgb: 192, 21, 47;
  --color-warning-rgb: 168, 75, 47;
  --color-info-rgb: 98, 108, 113;

  /* Typography */
  --font-family-base: "FKGroteskNeue", "Geist", "Inter", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-family-mono: "Berkeley Mono", ui-monospace, SFMono-Regular, Menlo,
    Monaco, Consolas, monospace;
  --font-size-xs: 11px;
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-md: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 18px;
  --font-size-2xl: 20px;
  --font-size-3xl: 24px;
  --font-size-4xl: 30px;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 550;
  --font-weight-bold: 600;
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;
  --letter-spacing-tight: -0.01em;

  /* Spacing */
  --space-0: 0;
  --space-1: 1px;
  --space-2: 2px;
  --space-4: 4px;
  --space-6: 6px;
  --space-8: 8px;
  --space-10: 10px;
  --space-12: 12px;
  --space-16: 16px;
  --space-20: 20px;
  --space-24: 24px;
  --space-32: 32px;

  /* Border Radius */
  --radius-sm: 6px;
  --radius-base: 8px;
  --radius-md: 10px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-xs: 0 1p
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\css\style.css`
- **Líneas:** 1321
- **Tamaño:** 37619 bytes

**Contenido:**
```css
:root {
  /* Primitive Color Tokens */
  --color-white: rgba(255, 255, 255, 1);
  --color-black: rgba(0, 0, 0, 1);
  --color-cream-50: rgba(252, 252, 249, 1);
  --color-cream-100: rgba(255, 255, 253, 1);
  --color-gray-200: rgba(245, 245, 245, 1);
  --color-gray-300: rgba(167, 169, 169, 1);
  --color-gray-400: rgba(119, 124, 124, 1);
  --color-slate-500: rgba(98, 108, 113, 1);
  --color-brown-600: rgba(94, 82, 64, 1);
  --color-charcoal-700: rgba(31, 33, 33, 1);
  --color-charcoal-800: rgba(38, 40, 40, 1);
  --color-slate-900: rgba(19, 52, 59, 1);
  --color-teal-300: rgba(50, 184, 198, 1);
  --color-teal-400: rgba(45, 166, 178, 1);
  --color-teal-500: rgba(33, 128, 141, 1);
  --color-teal-600: rgba(29, 116, 128, 1);
  --color-teal-700: rgba(26, 104, 115, 1);
  --color-teal-800: rgba(41, 150, 161, 1);
  --color-red-400: rgba(255, 84, 89, 1);
  --color-red-500: rgba(192, 21, 47, 1);
  --color-orange-400: rgba(230, 129, 97, 1);
  --color-orange-500: rgba(168, 75, 47, 1);

  /* RGB versions for opacity control */
  --color-brown-600-rgb: 94, 82, 64;
  --color-teal-500-rgb: 33, 128, 141;
  --color-slate-900-rgb: 19, 52, 59;
  --color-slate-500-rgb: 98, 108, 113;
  --color-red-500-rgb: 192, 21, 47;
  --color-red-400-rgb: 255, 84, 89;
  --color-orange-500-rgb: 168, 75, 47;
  --color-orange-400-rgb: 230, 129, 97;

  /* Background color tokens (Light Mode) */
  --color-bg-1: rgba(59, 130, 246, 0.08); /* Light blue */
  --color-bg-2: rgba(245, 158, 11, 0.08); /* Light yellow */
  --color-bg-3: rgba(34, 197, 94, 0.08); /* Light green */
  --color-bg-4: rgba(239, 68, 68, 0.08); /* Light red */
  --color-bg-5: rgba(147, 51, 234, 0.08); /* Light purple */
  --color-bg-6: rgba(249, 115, 22, 0.08); /* Light orange */
  --color-bg-7: rgba(236, 72, 153, 0.08); /* Light pink */
  --color-bg-8: rgba(6, 182, 212, 0.08); /* Light cyan */

  /* Semantic Color Tokens (Light Mode) */
  --color-background: var(--color-cream-50);
  --color-surface: var(--color-cream-100);
  --color-text: var(--color-slate-900);
  --color-text-secondary: var(--color-slate-500);
  --color-primary: var(--color-teal-500);
  --color-primary-hover: var(--color-teal-600);
  --color-primary-active: var(--color-teal-700);
  --color-secondary: rgba(var(--color-brown-600-rgb), 0.12);
  --color-secondary-hover: rgba(var(--color-brown-600-rgb), 0.2);
  --color-secondary-active: rgba(var(--color-brown-600-rgb), 0.25);
  --color-border: rgba(var(--color-brown-600-rgb), 0.2);
  --color-btn-primary-text: var(--color-cream-50);
  --color-card-border: rgba(var(--color-brown-600-rgb), 0.12);
  --color-card-border-inner: rgba(var(--color-brown-600-rgb), 0.12);
  --color-error: var(--color-red-500);
  --color-success: var(--color-teal-500);
  --color-warning: var(--color-orange-500);
  --color-info: var(--color-slate-500);
  --color-focus-ring: rgba(var(--color-teal-500-rgb), 0.4);
  --color-select-caret: rgba(var(--color-slate-900-rgb), 0.8);

  /* Common style patterns */
  --focus-ring: 0 0 0 3px var(--color-focus-ring);
  --focus-outline: 2px solid var(--color-primary);
  --status-bg-opacity: 0.15;
  --status-border-opacity: 0.25;
  --select-caret-light: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23134252' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --select-caret-dark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23f5f5f5' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");

  /* RGB versions for opacity control */
  --color-success-rgb: 33, 128, 141;
  --color-error-rgb: 192, 21, 47;
  --color-warning-rgb: 168, 75, 47;
  --color-info-rgb: 98, 108, 113;

  /* Typography */
  --font-family-base: "FKGroteskNeue", "Geist", "Inter", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-family-mono: "Berkeley Mono", ui-monospace, SFMono-Regular, Menlo,
    Monaco, Consolas, monospace;
  --font-size-xs: 11px;
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-md: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 18px;
  --font-size-2xl: 20px;
  --font-size-3xl: 24px;
  --font-size-4xl: 30px;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 550;
  --font-weight-bold: 600;
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;
  --letter-spacing-tight: -0.01em;

  /* Spacing */
  --space-0: 0;
  --space-1: 1px;
  --space-2: 2px;
  --space-4: 4px;
  --space-6: 6px;
  --space-8: 8px;
  --space-10: 10px;
  --space-12: 12px;
  --space-16: 16px;
  --space-20: 20px;
  --space-24: 24px;
  --space-32: 32px;

  /* Border Radius */
  --radius-sm: 6px;
  --radius-base: 8px;
  --radius-md: 10px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-xs: 0 1p
[... contenido truncado ...]
```

------------------------------------------------------------

### HTML (15 archivos)

#### `templates\admin_panel.html`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```html

```

------------------------------------------------------------

#### `templates\concursos.html`
- **Líneas:** 636
- **Tamaño:** 22619 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Concursos - UNIPAZ</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Roboto', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
            padding: 40px 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 50px;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
            animation: fadeInDown 0.6s ease;
        }

        .header p {
            font-size: 1rem;
            color: #b0b0d0;
            animation: fadeInUp 0.6s ease 0.1s both;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 30px;
            padding: 12px 24px;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            text-decoration: none;
            border-radius: 8px;
            border: 2px solid #667eea;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .back-btn:hover {
            background: rgba(102, 126, 234, 0.3);
            transform: translateX(-5px);
        }

        .tabs-container {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            animation: fadeIn 0.8s ease 0.2s both;
            flex-wrap: wrap;
        }

        .tab-btn {
            padding: 12px 24px;
            background: rgba(102, 126, 234, 0.15);
            color: #667eea;
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .tab-btn.active {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-color: #667eea;
        }

        .concursos-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 25px;
            animation: fadeIn 0.8s ease 0.3s both;
        }

        .concurso-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 25px;
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .concurso-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s ease;
        }

        .concurso-card:hover {
            transform: translateY(-12px);
            border-color: rgba(102, 126, 234, 0.6);
            box-shadow: 0 20px 50px rgba(102, 126, 234, 0.3);
        }

        .concurso-card:hover::before {
            left: 100%;
        }

        .concurso-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 15px;
            position: relative;
            z-index: 1;
        }

        .concurso-title h3 {
            font-size: 1.3rem;
            margin-bottom: 5px;
            color: #e0e0ff;
        }

        .concurso-title p {
            font-size: 0.85rem;
            color: #999;
        }

        .concurso-status {
            padding: 6px 12px;
            background: rgba(67, 233, 123, 0.2);
            color: #43e97b;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .concurso-status.proximo {
            background: rgba(255, 154, 86, 0.2);
            color: #ffaa66;
        }

        .concurso-status.finalizado {
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
        }

        .concurso-info {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 20px;
            position: relative;
            z-index: 1;
        }

        .info-item {
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            b
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\crear-examen.html`
- **Líneas:** 579
- **Tamaño:** 21841 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crear Examen - UNIPAZ</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="stylesheet" href="/static/css/math-panel.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
            padding: 2rem 0;
        }
        .navbar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem 2rem;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        .navbar-brand {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
            text-decoration: none;
        }
        .container {
            max-width: 1600px;
            margin: 0 auto;
            padding: 0 2rem;
        }
        .back-btn a {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            border: 2px solid #667eea;
            border-radius: 6px;
            text-decoration: none;
            margin-bottom: 2rem;
        }
        .page-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .page-header h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }
        .main-layout {
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 2rem;
        }
        .left-panel {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            height: fit-content;
            position: sticky;
            top: 2rem;
        }
        .left-panel h2 {
            color: #e0e0ff;
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
            border-bottom: 2px solid rgba(102, 126, 234, 0.5);
            padding-bottom: 1rem;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.4rem;
            color: #e0e0ff;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .form-group input,
        .form-group select {
            width: 100%;
            padding: 0.65rem;
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
            font-family: inherit;
            font-size: 0.9rem;
        }
        .form-group input:focus,
        .form-group select:focus {
            outline: none;
            border-color: #667eea;
            background: rgba(255, 255, 255, 0.15);
        }
        .form-group select option {
            background: #16213e;
            color: #ffffff;
        }
        .btn {
            padding: 0.7rem 1.2rem;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9rem;
            width: 100%;
            margin-top: 0.5rem;
        }
        .btn-primary {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            transition: all 0.3s ease;
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }
        .btn-primary:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }
        .codigo-acceso {
            margin-top: 1.5rem;
            padding: 1rem;
            background: rgba(76, 175, 80, 0.2);
            border-left: 4px solid #76d776;
            border-radius: 6px;
            display: none;
        }
        .codigo-acceso.show {
            display: block;
        }
        .codigo-acceso p {
            color: #76d776;
            font-size: 0.85rem;
            margin-bottom: 0.5rem;
        }
        .codigo-texto {
            background: rgba(0,0,0,0.3);
            padding: 0.75rem;
            border-radius: 6px;
            text-align: center;
            font-weight: bold;
            font-size: 1.1rem;
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\dashboard.html`
- **Líneas:** 162
- **Tamaño:** 5669 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - UNIPAZ</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <style>
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .stat-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 25px;
            text-align: center;
        }
        .stat-number {
            font-size: 2.5rem;
            color: #667eea;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .stat-label {
            color: #b0b0d0;
            font-size: 0.9rem;
        }
        .chart-container {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 25px;
            margin: 30px 0;
        }
        .progress {
            margin: 20px 0;
        }
        .progress-bar {
            height: 8px;
            background: rgba(102, 126, 234, 0.2);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 8px;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.3s ease;
        }
        .button-group {
            display: flex;
            gap: 10px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        .btn {
            padding: 10px 20px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }
        .btn-secondary {
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            border: 2px solid #667eea;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Mi Dashboard</h1>
            <p>Resumen de tu actividad y progreso</p>
        </div>

        <!-- ESTADÍSTICAS RÁPIDAS -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number" id="totalPuntos">0</div>
                <div class="stat-label">Puntos Totales</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="rachaActual">0🔥</div>
                <div class="stat-label">Racha Actual</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="porcentajeExito">0%</div>
                <div class="stat-label">% Éxito</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="nivel">1</div>
                <div class="stat-label">Nivel</div>
            </div>
        </div>

        <!-- PROGRESO POR MATERIA -->
        <div class="chart-container">
            <h3>Progreso por Materia</h3>
            <div id="materiasList"></div>
        </div>

        <!-- ÚLTIMOS LOGROS -->
        <div class="chart-container">
            <h3>Últimos Logros Desbloqueados</h3>
            <div id="logrosList" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 15px;"></div>
        </div>

        <!-- ACCIONES -->
        <div class="chart-container">
            <h3>Acciones</h3>
            <div class="button-group">
                <button class="btn" onclick="irA('/quiz')">📝 Hacer Quiz</button>
                <button class="btn btn-secondary" onclick="irA('/rankings')">🏆 Ver Rankings</button>
                <button class="btn btn-secondary" onclick="irA('/concursos')">⚔️ Participar Concurso</button>
            </div>
        </div>
    </div>

    <script src="/static/js/main.js"></script>
    <script src="/static/js/utils.js"></script>
    <script>
        function irA(url) {
            window.location.href = url;
        }

        async function cargarDashboard() {
            try {
                const usuario = AUTH.obtenerUsuarioActual();
                if (!usuario) {
                    window.location.href = '/login';
                    return;
                }

                // Cargar datos del usuario
                const response = await fetch(`/api/usuarios/${usuario.id}`);
                const datos = await response.json();

                // Actualizar estadísticas
                document.getElementById
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\debug-examen.html`
- **Líneas:** 309
- **Tamaño:** 11414 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Debug - Unirse a Examen</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #f0f0f0;
            padding: 2rem;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        h1 {
            text-align: center;
            margin-bottom: 2rem;
            color: #667eea;
            font-size: 2.5rem;
        }
        
        .controls {
            background: rgba(102, 126, 234, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            display: grid;
            grid-template-columns: 1fr auto auto;
            gap: 1rem;
            align-items: center;
        }
        
        .controls label {
            color: #e0e0ff;
            font-weight: bold;
            font-size: 1.1rem;
        }
        
        input {
            padding: 0.75rem 1rem;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 6px;
            color: #ffffff;
            font-family: monospace;
            font-size: 1rem;
        }
        
        input:focus {
            outline: none;
            border-color: #667eea;
            background: rgba(255, 255, 255, 0.15);
        }
        
        button {
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }
        
        button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }
        
        .logs-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }
        
        .log-section {
            background: rgba(102, 126, 234, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 12px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            max-height: 600px;
        }
        
        .log-header {
            background: rgba(102, 126, 234, 0.3);
            padding: 1rem;
            font-weight: bold;
            font-size: 1.1rem;
            color: #e0e0ff;
            border-bottom: 2px solid rgba(102, 126, 234, 0.3);
        }
        
        .log {
            flex: 1;
            overflow-y: auto;
            padding: 1rem;
            font-size: 0.9rem;
            line-height: 1.6;
        }
        
        .log-entry {
            padding: 0.5rem;
            margin-bottom: 0.5rem;
            border-radius: 4px;
            border-left: 3px solid transparent;
        }
        
        .log-entry.info {
            background: rgba(100, 150, 255, 0.1);
            border-left-color: #667eea;
            color: #b0d4ff;
        }
        
        .log-entry.success {
            background: rgba(76, 175, 80, 0.1);
            border-left-color: #4caf50;
            color: #81c784;
        }
        
        .log-entry.error {
            background: rgba(244, 67, 54, 0.1);
            border-left-color: #f44336;
            color: #ef5350;
        }
        
        .log-entry.warning {
            background: rgba(255, 193, 7, 0.1);
            border-left-color: #ffc107;
            color: #fdd835;
        }
        
        .timestamp {
            color: #888;
            font-size: 0.8rem;
            display: inline-block;
            min-width: 80px;
        }
        
        @media (max-width: 1200px) {
            .logs-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔧 Debug Examen - UNIPAZ</h1>
        
        <div class="controls">
            <label>Código (12 caracteres):</label>
            <input type="text" id="codigo" value="0CEA79DADFAD" maxlength="12" placeholder="Ej: A1B2C3D4E5F6">
            <button onclick="buscarExamen()">🔍 Buscar Examen</button>
            <button onclick="cargarPreguntas()" id="btnCargar" disabled>📥 Cargar Preguntas</button>
        </div>

        <div class="logs-container">
            <div class="log-section">
                <div class="log-header">📨 Respuestas de API</
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\duelo.html`
- **Líneas:** 472
- **Tamaño:** 14989 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duelo 1vs1 - UNIPAZ</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Roboto', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        /* ===== HEADER DUELO ===== */
        .duelo-header {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 30px;
            animation: fadeInDown 0.6s ease;
        }

        .duelo-info {
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            gap: 30px;
            align-items: center;
        }

        .jugador {
            text-align: center;
        }

        .jugador-avatar {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            margin: 0 auto 12px;
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }

        .jugador-nombre {
            font-weight: 700;
            color: #e0e0ff;
            margin-bottom: 5px;
        }

        .jugador-carrera {
            font-size: 0.85rem;
            color: #b0b0d0;
        }

        .vs-container {
            text-align: center;
        }

        .vs-text {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .ronda-info {
            font-size: 0.9rem;
            color: #b0b0d0;
            margin-top: 10px;
        }

        /* ===== TIMER ===== */
        .timer-container {
            text-align: center;
            margin-bottom: 30px;
        }

        .timer {
            font-size: 3rem;
            font-weight: 700;
            color: #667eea;
            text-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
            animation: pulse 1s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .timer-label {
            font-size: 0.9rem;
            color: #b0b0d0;
            margin-top: 8px;
        }

        /* ===== PREGUNTA SECTION ===== */
        .pregunta-section {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 30px;
            margin-bottom: 30px;
            animation: fadeInUp 0.6s ease 0.1s both;
        }

        .pregunta-numero {
            font-size: 0.9rem;
            color: #b0b0d0;
            margin-bottom: 15px;
        }

        .pregunta-texto {
            font-size: 1.4rem;
            font-weight: 600;
            color: #e0e0ff;
            margin-bottom: 30px;
            line-height: 1.6;
        }

        /* ===== OPCIONES ===== */
        .opciones-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-bottom: 25px;
        }

        .opcion-btn {
            padding: 20px;
            background: rgba(102, 126, 234, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            color: #e0e0ff;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            font-size: 1rem;
            text-align: left;
        }

        .opcion-btn:hover {
            background: rgba(102, 126, 234, 0.2);
            border-color: rgba(102, 126, 234, 0.6);
            transform: translateY(-2px);
        }

        .opcion-btn.seleccionada {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-color: #667eea;
        }

        .opcion-btn.correcta {
            background: linear-gradient(135deg, #43e97b, #38f9d7);
            border-color: #43e97b;
            color: white;
        }

        .opcion-btn.incorrecta {
            background: linear-gradient(135deg, #f5576c, #ff6a88);
            border-color: #f5576c;
            color: white;
        }

        /* ===== RESULTADO SCREEN ===== */
        .resultado-screen {
  
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\index.html`
- **Líneas:** 891
- **Tamaño:** 29674 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UNIPAZ - Sistema de Quizzes</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="stylesheet" href="/static/css/animations.css">
    <link rel="stylesheet" href="/static/css/responsive.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
        }

        .navbar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .navbar-brand {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: opacity 0.3s ease;
            padding: 0.5rem 1rem;
            border-radius: 4px;
        }

        .nav-links a:hover {
            background: rgba(255,255,255,0.2);
            opacity: 0.9;
        }

        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .hero-section {
            text-align: center;
            margin-bottom: 3rem;
            animation: fadeInDown 0.8s ease;
        }

        .hero-section h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-section p {
            font-size: 1.1rem;
            color: #b0b0d0;
            margin-bottom: 2rem;
        }

        .main-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .option-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 12px;
            padding: 2rem;
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            animation: fadeInUp 0.8s ease;
        }

        .option-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s ease;
        }

        .option-card:hover {
            transform: translateY(-8px);
            border-color: rgba(102, 126, 234, 0.6);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.25);
        }

        .option-card:hover::before {
            left: 100%;
        }

        .card-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .option-card h2 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #e0e0ff;
        }

        .option-card p {
            color: #b0b0d0;
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }

        .card-buttons {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            flex: 1;
            min-width: 120px;
            font-size: 0.9rem;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }

        .btn-secondary {
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            border: 2px solid #667eea;
        }

        .btn-secondary:hover {
            background: rgba(102, 126, 234, 0.3);
        }

        .modal {
            display: none;
            position: fixed;
           
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\login.html`
- **Líneas:** 277
- **Tamaño:** 8444 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - UNIPAZ</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #f0f0f0;
            padding: 20px;
        }
        
        .login-container {
            width: 100%;
            max-width: 450px;
            background: rgba(30, 30, 50, 0.95);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 40px;
            animation: slideUp 0.6s ease;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .logo-icon {
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 35px;
            margin: 0 auto 15px;
        }
        
        h1 {
            color: #e0e0ff;
            margin-bottom: 10px;
        }
        
        p {
            color: #b0b0d0;
            font-size: 0.95rem;
        }
        
        .form-group {
            margin-bottom: 18px;
        }
        
        label {
            display: block;
            color: #e0e0ff;
            font-weight: 600;
            margin-bottom: 8px;
            font-size: 0.9rem;
        }
        
        input {
            width: 100%;
            padding: 12px;
            background: rgba(102, 126, 234, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            color: #f0f0f0;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        input:focus {
            outline: none;
            border-color: #667eea;
            background: rgba(102, 126, 234, 0.15);
            box-shadow: 0 0 15px rgba(102, 126, 234, 0.2);
        }
        
        input::placeholder {
            color: #999;
        }
        
        .error {
            background: rgba(245, 87, 108, 0.2);
            border-left: 4px solid #f5576c;
            color: #ff9999;
            padding: 12px;
            border-radius: 4px;
            margin-bottom: 20px;
            display: none;
            font-size: 0.9rem;
        }
        
        .error.mostrar {
            display: block;
        }
        
        .btn-login {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 700;
            font-size: 1rem;
            transition: all 0.3s ease;
            margin-bottom: 15px;
        }
        
        .btn-login:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        }
        
        .btn-login:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        
        .btn-register {
            width: 100%;
            padding: 14px;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            border: 2px solid #667eea;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            font-size: 1rem;
            text-decoration: none;
            display: block;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .btn-register:hover {
            background: rgba(102, 126, 234, 0.3);
        }
        
        .demo-section {
            background: rgba(67, 233, 123, 0.1);
            border: 1px solid #43e97b;
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
        }
        
        .demo-section h4 {
            color: #43e97b;
            margin-bottom: 10px;
            font-size: 0.9rem;
        }
        
        .demo-section p {
            color: #b0d0d0;
            font-size: 0.85rem;
            line-height: 1.5;
        }
        
        .demo-btn {
            width: 100%;
            padding: 10px;
            background: #43e97b;
            color: #0f0f1e;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            margin-top: 10px;
            transition: all 0.3s ease;
        }
        
        .demo-btn:hover {
            opacity: 0.9;
            transform: translateY(-2px);
        }
        
        @keyframes slideUp {
            from { opacity: 0
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\logros.html`
- **Líneas:** 462
- **Tamaño:** 15854 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mis Logros - UNIPAZ</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Roboto', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
            padding: 40px 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 50px;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
            animation: fadeInDown 0.6s ease;
        }

        .header p {
            font-size: 1rem;
            color: #b0b0d0;
            animation: fadeInUp 0.6s ease 0.1s both;
        }

        /* ===== TABS ===== */
        .tabs-container {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            animation: fadeIn 0.8s ease 0.2s both;
            flex-wrap: wrap;
        }

        .tab-btn {
            padding: 12px 24px;
            background: rgba(102, 126, 234, 0.15);
            color: #667eea;
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .tab-btn.active {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-color: #667eea;
        }

        /* ===== LOGROS GRID ===== */
        .logros-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 25px;
            animation: fadeIn 0.8s ease 0.3s both;
        }

        .logro-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 25px;
            text-align: center;
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            min-height: 250px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .logro-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s ease;
        }

        .logro-card:hover {
            transform: translateY(-12px);
            border-color: rgba(102, 126, 234, 0.6);
            box-shadow: 0 20px 50px rgba(102, 126, 234, 0.3);
        }

        .logro-card:hover::before {
            left: 100%;
        }

        .logro-icon {
            font-size: 64px;
            margin-bottom: 15px;
            position: relative;
            z-index: 1;
            animation: bounce 1s ease-in-out infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .logro-card h3 {
            font-size: 1.2rem;
            margin-bottom: 10px;
            color: #e0e0ff;
            position: relative;
            z-index: 1;
        }

        .logro-card p {
            font-size: 0.85rem;
            color: #b0b0d0;
            margin-bottom: 12px;
            position: relative;
            z-index: 1;
            line-height: 1.4;
        }

        .logro-fecha {
            font-size: 0.75rem;
            color: #999;
            position: relative;
            z-index: 1;
        }

        /* Logro Desbloqueado */
        .logro-card.desbloqueado {
            background: linear-gradient(135deg, rgba(67, 233, 123, 0.15) 0%, rgba(56, 249, 215, 0.15) 100%);
            border-color: rgba(67, 233, 123, 0.5);
        }

        .logro-card.desbloqueado .logro-icon {
            filter: drop-shadow(0 0 10px rgba(67, 233, 123, 0.5));
        }

        /* Logro Bloqueado */
        .logro-card.bloqueado {
            background: linear-gradient(135deg, rgba(100, 100, 120, 0.1) 0%, rgba(80, 80, 100, 0.1) 100%);
            border-color: rgba(100, 100, 120, 0.3);
            opacity: 0.6;
        }

        .logro-card.bloqueado .logro-icon {
            opacity: 0.4;
 
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\materias.html`
- **Líneas:** 418
- **Tamaño:** 13421 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Materias - UNIPAZ</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Roboto', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
            padding: 40px 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 30px;
            padding: 12px 24px;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            text-decoration: none;
            border-radius: 8px;
            border: 2px solid #667eea;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .back-btn:hover {
            background: rgba(102, 126, 234, 0.3);
            transform: translateX(-5px);
        }

        .header {
            text-align: center;
            margin-bottom: 50px;
            animation: fadeInDown 0.6s ease;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
        }

        .header p {
            font-size: 1rem;
            color: #b0b0d0;
        }

        /* ===== CARRERA HEADER ===== */
        .carrera-header {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 30px;
            margin-bottom: 40px;
            display: flex;
            align-items: center;
            gap: 25px;
            animation: fadeInUp 0.6s ease 0.1s both;
        }

        .carrera-icon {
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        }

        .carrera-info h2 {
            font-size: 1.8rem;
            margin-bottom: 8px;
            color: #e0e0ff;
        }

        .carrera-info p {
            color: #b0b0d0;
            font-size: 0.95rem;
        }

        /* ===== TABS POR SEMESTRE ===== */
        .semestre-tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            flex-wrap: wrap;
            animation: fadeIn 0.8s ease 0.2s both;
        }

        .semestre-btn {
            padding: 12px 24px;
            background: rgba(102, 126, 234, 0.15);
            color: #667eea;
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .semestre-btn:hover, .semestre-btn.active {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-color: #667eea;
        }

        /* ===== MATERIAS GRID ===== */
        .materias-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 25px;
            animation: fadeIn 0.8s ease 0.3s both;
        }

        .materia-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 25px;
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            min-height: 220px;
            display: flex;
            flex-direction: column;
        }

        .materia-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s ease;
        }

        .materia-card:hover {
            transform: translateY(-12px);
            border-color: rgba(102, 126, 234, 0.6);
            box-shadow: 0 20px 50px rgba(102, 126, 234, 0.3);
        }

        .materia-card:hover::before {
            left: 100%;
        }

        .materia-icon {
            font-size: 40px
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\perfil.html`
- **Líneas:** 516
- **Tamaño:** 18681 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Perfil - UNIPAZ</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Roboto', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
            padding: 40px 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 30px;
            padding: 12px 24px;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            text-decoration: none;
            border-radius: 8px;
            border: 2px solid #667eea;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .back-btn:hover {
            background: rgba(102, 126, 234, 0.3);
            transform: translateX(-5px);
        }

        /* ===== PROFILE HEADER ===== */
        .profile-header {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 40px;
            display: grid;
            grid-template-columns: auto 1fr auto;
            gap: 30px;
            align-items: center;
            margin-bottom: 40px;
            animation: fadeInDown 0.6s ease;
        }

        .avatar-section {
            text-align: center;
        }

        .avatar {
            width: 120px;
            height: 120px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 64px;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
            margin-bottom: 15px;
        }

        .change-avatar {
            font-size: 0.85rem;
            color: #667eea;
            cursor: pointer;
            text-decoration: underline;
        }

        .profile-info h2 {
            font-size: 2rem;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .profile-info p {
            color: #b0b0d0;
            font-size: 0.95rem;
            margin-bottom: 5px;
        }

        .level-badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 600;
            margin-top: 10px;
        }

        .edit-btn {
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .edit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        }

        /* ===== TABS ===== */
        .tabs-container {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            border-bottom: 2px solid rgba(102, 126, 234, 0.2);
            flex-wrap: wrap;
        }

        .tab-btn {
            padding: 12px 24px;
            background: transparent;
            color: #b0b0d0;
            border: none;
            border-bottom: 3px solid transparent;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .tab-btn:hover {
            color: #667eea;
        }

        .tab-btn.active {
            color: #667eea;
            border-bottom-color: #667eea;
        }

        /* ===== STATS GRID ===== */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }

        .stat-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 20px;
            text-align: center;
        }

        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 8px;
        }

        .stat-label {
            color: #b0b0d0;
            font-size: 0.9rem;
        }

        /* =====
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\quiz.html`
- **Líneas:** 483
- **Tamaño:** 15541 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz - UNIPAZ</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
        }

        .navbar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .navbar-brand {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .container {
            max-width: 900px;
            margin: 2rem auto;
            padding: 2rem;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header h1 {
            font-size: 2rem;
            color: white;
        }

        .stats {
            display: flex;
            gap: 1.5rem;
            font-size: 0.95rem;
        }

        .stat {
            background: rgba(255,255,255,0.2);
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
        }

        .stat-label {
            font-size: 0.85rem;
            opacity: 0.9;
        }

        .stat-value {
            font-size: 1.2rem;
            font-weight: 700;
            margin-top: 0.25rem;
        }

        .btn-volver {
            background: rgba(255,255,255,0.2);
            color: white;
            border: 2px solid rgba(255,255,255,0.5);
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .btn-volver:hover {
            background: rgba(255,255,255,0.3);
            border-color: rgba(255,255,255,0.8);
        }

        .quiz-container {
            background: rgba(102, 126, 234, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .pregunta {
            margin-bottom: 2rem;
        }

        .pregunta-texto {
            font-size: 1.3rem;
            color: #e0e0ff;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }

        .opciones {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem;
        }

        .opcion {
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(255, 255, 255, 0.3);
            padding: 1rem;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #e0e0ff;
            font-weight: 500;
        }

        .opcion:hover {
            background: rgba(255, 255, 255, 0.2);
            border-color: rgba(255, 255, 255, 0.6);
            transform: translateX(8px);
        }

        .opcion.seleccionada {
            background: rgba(102, 126, 234, 0.4);
            border-color: #667eea;
        }

        .opcion.correcta {
            background: rgba(76, 175, 80, 0.3);
            border-color: #4caf50;
        }

        .opcion.incorrecta {
            background: rgba(244, 67, 54, 0.3);
            border-color: #f44336;
        }

        .botones {
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin-top: 2rem;
        }

        .btn {
            padding: 0.75rem 2rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            font-size: 1rem;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }

        .btn-primary:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .error {
            background: rgba(244, 67, 54, 0.2);
            border: 2px solid #f44336;
            padding: 1.5rem;
            border-radius: 8px;
            color: #ffb3ba;
            margin: 2rem 0;
            text-align: center;
        }

        .error a {
            colo
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\rankings.html`
- **Líneas:** 325
- **Tamaño:** 9859 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rankings - UNIPAZ</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
            padding: 2rem 0;
        }
        
        .navbar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem 2rem;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        
        .navbar-brand {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
            text-decoration: none;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }
        
        .back-btn {
            margin-bottom: 2rem;
        }
        
        .back-btn a {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            border: 2px solid #667eea;
            border-radius: 6px;
            text-decoration: none;
        }
        
        .back-btn a:hover {
            background: rgba(102, 126, 234, 0.3);
        }
        
        .page-header {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .page-header h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }
        
        .page-header p {
            color: #b0b0d0;
            font-size: 1.1rem;
        }
        
        .rankings-table {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .table-header {
            background: rgba(102, 126, 234, 0.3);
            padding: 1.5rem;
            display: grid;
            grid-template-columns: 80px 150px 1fr 150px 150px;
            gap: 1rem;
            align-items: center;
            font-weight: bold;
            color: #e0e0ff;
            border-bottom: 2px solid rgba(102, 126, 234, 0.3);
        }
        
        .table-body {
            max-height: 700px;
            overflow-y: auto;
        }
        
        .table-row {
            padding: 1rem 1.5rem;
            display: grid;
            grid-template-columns: 80px 150px 1fr 150px 150px;
            gap: 1rem;
            align-items: center;
            border-bottom: 1px solid rgba(102, 126, 234, 0.2);
            transition: all 0.3s ease;
        }
        
        .table-row:hover {
            background: rgba(102, 126, 234, 0.15);
        }
        
        .posicion {
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
        }
        
        .posicion.top1 { color: #ffd700; }
        .posicion.top2 { color: #c0c0c0; }
        .posicion.top3 { color: #cd7f32; }
        
        .estudiante {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: white;
            font-size: 0.9rem;
        }
        
        .nombre {
            color: #e0e0ff;
            font-weight: 600;
        }
        
        .carrera {
            color: #b0b0d0;
            font-size: 0.9rem;
        }
        
        .racha {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            justify-content: center;
        }
        
        .racha-number {
            color: #ffd700;
            font-weight: bold;
            font-size: 1.1rem;
        }
        
        .puntos {
            text-align: right;
            color: #81c784;
            font-weight: bold;
            font-size: 1.1rem;
        }
        
        .loading {
            text-align: center;
            padding: 3rem;
            color: #b0b0d0;
        }
        
        .error {
            background: rgba(244, 67, 54, 0.1);
            border: 2px solid rgba(244, 67, 54, 0.3);
            border-radius: 
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\registro.html`
- **Líneas:** 345
- **Tamaño:** 11593 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro - UNIPAZ</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #f0f0f0;
            padding: 20px;
        }
        
        .register-container {
            width: 100%;
            max-width: 500px;
            background: rgba(30, 30, 50, 0.95);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            padding: 40px;
            animation: slideUp 0.6s ease;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .logo-icon {
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 35px;
            margin: 0 auto 15px;
        }
        
        h1 {
            color: #e0e0ff;
            margin-bottom: 10px;
        }
        
        p {
            color: #b0b0d0;
            font-size: 0.95rem;
        }
        
        .form-group {
            margin-bottom: 18px;
        }
        
        label {
            display: block;
            color: #e0e0ff;
            font-weight: 600;
            margin-bottom: 8px;
            font-size: 0.9rem;
        }
        
        input, select {
            width: 100%;
            padding: 12px;
            background: rgba(102, 126, 234, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 8px;
            color: #f0f0f0;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        input:focus, select:focus {
            outline: none;
            border-color: #667eea;
            background: rgba(102, 126, 234, 0.15);
            box-shadow: 0 0 15px rgba(102, 126, 234, 0.2);
        }
        
        input::placeholder {
            color: #999;
        }
        
        select option {
            background: #1a1a2e;
            color: #f0f0f0;
            padding: 10px;
        }
        
        .error {
            background: rgba(245, 87, 108, 0.2);
            border-left: 4px solid #f5576c;
            color: #ff9999;
            padding: 12px;
            border-radius: 4px;
            margin-bottom: 20px;
            display: none;
            font-size: 0.9rem;
        }
        
        .error.mostrar {
            display: block;
        }
        
        .success {
            background: rgba(67, 233, 123, 0.2);
            border-left: 4px solid #43e97b;
            color: #9affab;
            padding: 12px;
            border-radius: 4px;
            margin-bottom: 20px;
            display: none;
            font-size: 0.9rem;
        }
        
        .success.mostrar {
            display: block;
        }
        
        .btn-register {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 700;
            font-size: 1rem;
            transition: all 0.3s ease;
            margin-bottom: 15px;
        }
        
        .btn-register:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        }
        
        .btn-register:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        
        .btn-login {
            width: 100%;
            padding: 14px;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            border: 2px solid #667eea;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            font-size: 1rem;
            text-decoration: none;
            display: block;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .btn-login:hover {
            background: rgba(102, 126, 234, 0.3);
        }
        
        .password-requirements {
            background: rgba(102, 126, 234, 0.1);
            border: 1px solid rgba(102, 126, 234, 0.3);
            border-radius: 6px;
            padding: 10px;
            margin-top: 5px;
            font-size: 0.8rem;
            color: #b0b0d0;
        }
        
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
   
[... contenido truncado ...]
```

------------------------------------------------------------

#### `templates\unirse-examen.html`
- **Líneas:** 518
- **Tamaño:** 18636 bytes

**Contenido:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unirse a Examen - UNIPAZ</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #f0f0f0;
            padding: 2rem 0;
        }
        .navbar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem 2rem;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        .navbar-brand {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
            text-decoration: none;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }
        .back-btn a {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            border: 2px solid #667eea;
            border-radius: 6px;
            text-decoration: none;
            margin-bottom: 2rem;
        }
        .page-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .page-header h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }
        .main-content {
            display: grid;
            grid-template-columns: 350px 1fr;
            gap: 2rem;
            margin-bottom: 2rem;
        }
        .search-panel {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            height: fit-content;
            position: sticky;
            top: 2rem;
        }
        .search-panel h2 {
            color: #e0e0ff;
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
            border-bottom: 2px solid rgba(102, 126, 234, 0.5);
            padding-bottom: 1rem;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.4rem;
            color: #e0e0ff;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .form-group input {
            width: 100%;
            padding: 0.65rem;
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
            font-family: inherit;
            font-size: 0.9rem;
            text-transform: uppercase;
        }
        .form-group input:focus {
            outline: none;
            border-color: #667eea;
            background: rgba(255, 255, 255, 0.15);
        }
        .btn {
            padding: 0.7rem 1.2rem;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9rem;
            width: 100%;
            margin-top: 0.5rem;
            transition: all 0.3s ease;
        }
        .btn-primary {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }
        .btn-primary:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }
        .examen-info {
            background: linear-gradient(135deg, rgba(76, 175, 80, 0.2) 0%, rgba(76, 175, 80, 0.1) 100%);
            border: 2px solid rgba(76, 175, 80, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 1.5rem;
            display: none;
        }
        .examen-info.show {
            display: block;
        }
        .examen-info p {
            color: #e0e0ff;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
        }
        .examen-info strong {
            color: #76d776;
        }
        .examen-details {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 12px;
            paddi
[... contenido truncado ...]
```

------------------------------------------------------------

### JSON (6 archivos)

#### `rutas.json`
- **Líneas:** 114
- **Tamaño:** 1770 bytes

**Contenido:**
```json
[
  {
    "endpoint": "index",
    "methods": [
      "GET"
    ],
    "url": "/"
  },
  {
    "endpoint": "get_carreras",
    "methods": [
      "GET"
    ],
    "url": "/api/carreras"
  },
  {
    "endpoint": "health",
    "methods": [
      "GET"
    ],
    "url": "/api/health"
  },
  {
    "endpoint": "api_login",
    "methods": [
      "POST"
    ],
    "url": "/api/login"
  },
  {
    "endpoint": "get_materias",
    "methods": [
      "GET"
    ],
    "url": "/api/materias"
  },
  {
    "endpoint": "get_materias_por_carrera",
    "methods": [
      "GET"
    ],
    "url": "/api/materias/carrera/<int:carrera_id>"
  },
  {
    "endpoint": "get_preguntas",
    "methods": [
      "GET"
    ],
    "url": "/api/quiz/preguntas/<int:materia_id>"
  },
  {
    "endpoint": "rankings_racha",
    "methods": [
      "GET"
    ],
    "url": "/api/rankings/global/racha"
  },
  {
    "endpoint": "api_register",
    "methods": [
      "POST"
    ],
    "url": "/api/register"
  },
  {
    "endpoint": "concursos",
    "methods": [
      "GET"
    ],
    "url": "/concursos"
  },
  {
    "endpoint": "dashboard",
    "methods": [
      "GET"
    ],
    "url": "/dashboard"
  },
  {
    "endpoint": "login",
    "methods": [
      "GET"
    ],
    "url": "/login"
  },
  {
    "endpoint": "quiz",
    "methods": [
      "GET"
    ],
    "url": "/quiz"
  },
  {
    "endpoint": "rankings",
    "methods": [
      "GET"
    ],
    "url": "/rankings"
  },
  {
    "endpoint": "registro",
    "methods": [
      "GET"
    ],
    "url": "/registro"
  },
  {
    "endpoint": "static",
    "methods": [
      "GET"
    ],
    "url": "/static/<path:filename>"
  }
]
```

------------------------------------------------------------

#### `rutas_y_redirecciones.json`
- **Líneas:** 150
- **Tamaño:** 2940 bytes

**Contenido:**
```json
{
  "rutas": [
    {
      "tipo": "ruta",
      "endpoint": "static",
      "url": "/static/<path:filename>",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "index",
      "url": "/",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "login",
      "url": "/login",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "registro",
      "url": "/registro",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "quiz",
      "url": "/quiz",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "rankings",
      "url": "/rankings",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "concursos",
      "url": "/concursos",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "dashboard",
      "url": "/dashboard",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "api_login",
      "url": "/api/login",
      "métodos": [
        "POST"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "api_register",
      "url": "/api/register",
      "métodos": [
        "POST"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "get_carreras",
      "url": "/api/carreras",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "get_materias",
      "url": "/api/materias",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "get_materias_por_carrera",
      "url": "/api/materias/carrera/<int:carrera_id>",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "get_preguntas",
      "url": "/api/quiz/preguntas/<int:materia_id>",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "rankings_racha",
      "url": "/api/rankings/global/racha",
      "métodos": [
        "GET"
      ]
    },
    {
      "tipo": "ruta",
      "endpoint": "health",
      "url": "/api/health",
      "métodos": [
        "GET"
      ]
    }
  ],
  "redirecciones": [
    {
      "tipo": "redirección",
      "archivo": ".\\export_routes.py",
      "línea": 24,
      "destino": "/ruta",
      "código": "r'redirect\\([\\'\"]([^\\'\"]+)[\\'\"]\\)',  # redirect('/ruta')"
    },
    {
      "tipo": "redirección",
      "archivo": ".\\export_routes.py",
      "línea": 25,
      "destino": "endpoint",
      "código": "r'redirect\\(url_for\\([\\'\"]([^\\'\"]+)[\\'\"]\\)',  # redirect(url_for('endpoint'))"
    }
  ],
  "total_rutas": 16,
  "total_redirecciones": 2
}
```

------------------------------------------------------------

#### `static\data\carreras.json`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```json

```

------------------------------------------------------------

#### `static\data\config.json`
- **Líneas:** 233
- **Tamaño:** 5617 bytes

**Contenido:**
```json
{
  "app": {
    "nombre": "UNIPAZ Quiz System",
    "version": "1.0.0",
    "descripcion": "Sistema interactivo de exámenes para estudiantes de la Universidad de la Paz",
    "autor": "UNIPAZ",
    "ano": 2025
  },
  "api": {
    "baseUrl": "http://localhost:5000",
    "apiUrl": "http://localhost:5000/api",
    "timeout": 30000,
    "retryAttempts": 3
  },
  "colores": {
    "primario": "#667eea",
    "secundario": "#764ba2",
    "acento": "#f093fb",
    "exito": "#43e97b",
    "error": "#f5576c",
    "advertencia": "#ff9a56",
    "info": "#00f2fe"
  },
  "carreras": [
    {
      "id": 1,
      "nombre": "Ingeniería",
      "subtitulo": "Informática",
      "color": "#667eea",
      "icono": "⚙️",
      "descripcion": "Programa de ingeniería en informática"
    },
    {
      "id": 2,
      "nombre": "Medicina",
      "subtitulo": "Ciencias de la Salud",
      "color": "#f5576c",
      "icono": "🏥",
      "descripcion": "Programa de medicina general"
    },
    {
      "id": 3,
      "nombre": "Derecho",
      "subtitulo": "Ciencias Jurídicas",
      "color": "#43e97b",
      "icono": "⚖️",
      "descripcion": "Programa de derecho"
    },
    {
      "id": 4,
      "nombre": "Administración",
      "subtitulo": "Negocios",
      "color": "#ff9a56",
      "icono": "📊",
      "descripcion": "Programa de administración empresarial"
    },
    {
      "id": 5,
      "nombre": "Psicología",
      "subtitulo": "Ciencias del Comportamiento",
      "color": "#00f2fe",
      "icono": "🧠",
      "descripcion": "Programa de psicología"
    },
    {
      "id": 6,
      "nombre": "Educación",
      "subtitulo": "Pedagogía",
      "color": "#fee140",
      "icono": "🎓",
      "descripcion": "Programa de educación"
    },
    {
      "id": 7,
      "nombre": "Economía",
      "subtitulo": "Ciencias Económicas",
      "color": "#a8edea",
      "icono": "💰",
      "descripcion": "Programa de economía"
    },
    {
      "id": 8,
      "nombre": "Ciencias",
      "subtitulo": "Investigación Científica",
      "color": "#12c2e9",
      "icono": "🔬",
      "descripcion": "Programa de ciencias"
    }
  ],
  "quiz": {
    "modos": [
      {
        "id": "normal",
        "nombre": "Normal",
        "icono": "🎮",
        "descripcion": "100 preguntas progresivas. Ideal para aprender.",
        "dificultad": "medio",
        "cantidad": 100,
        "tiempoRespuesta": 60
      },
      {
        "id": "hardcore",
        "nombre": "Hardcore",
        "icono": "⚡",
        "descripcion": "Elige dificultad. Un error y vuelves a empezar.",
        "dificultades": ["facil", "medio", "dificil"],
        "vidas": 3,
        "tiempoRespuesta": 30
      },
      {
        "id": "pesadilla",
        "nombre": "Pesadilla",
        "icono": "💀",
        "descripcion": "10 niveles consecutivos sin errores. ¡Desafío extremo!",
        "dificultad": "dificil",
        "cantidad": 10,
        "vidas": 1,
        "tiempoRespuesta": 20
      }
    ]
  },
  "logros": [
    {
      "id": 1,
      "nombre": "Principiante",
      "icono": "🥇",
      "categoria": "inicio",
      "requisito": "Completar primer quiz",
      "puntos": 10
    },
    {
      "id": 2,
      "nombre": "En Racha",
      "icono": "🔥",
      "categoria": "racha",
      "requisito": "10 respuestas correctas consecutivas",
      "puntos": 25
    },
    {
      "id": 3,
      "nombre": "Racha Legendaria",
      "icono": "🔥🔥🔥",
      "categoria": "racha",
      "requisito": "50 respuestas correctas consecutivas",
      "puntos": 100
    },
    {
      "id": 4,
      "nombre": "Maestro",
      "icono": "💎",
      "categoria": "maestria",
      "requisito": "100% de éxito en una materia",
      "puntos": 75
    },
    {
      "id": 5,
      "nombre": "Campeón",
      "icono": "🏆",
      "categoria": "concurso",
      "requisito": "Ganar un torneo por eliminación",
      "puntos": 150
    }
  ],
  "animaciones": {
    "duracionRapida": 300,
    "duracionMedia": 600,
    "duracionLenta": 1000,
    "tiempoEspera": 2000
  },
  "notificaciones": {
    "duracionCorta": 2000,
    "duracionMedia": 3000,
    "duracionLarga": 5000,
    "posicion": "top-right"
  },
  "ranking": {
    "topElementos": 10,
    "actualizacionCada": 30000,
    "mostrarPosicion": true
  },
  "concursos": {
    "tiempoRespuesta": 30,
    "maxParticipantes": 32,
    "tipos": ["eliminacion", "liga", "grupal"],
    "premios": {
      "primero": 50,
      "segundo": 30,
      "tercero": 15
    }
  },
  "usuario": {
    "nivelMinimo": 1,
    "nivelMaximo": 100,
    "xpPorNivel": 1000,
    "streamingRachas": true,
    "sincronizarEnLinea": true
  },
  "seguridad": {
    "requerirLogin": true,
    "duracionSesion": 3600000,
    "recordarUsuario": true
  },
  "base_datos": {
    "host": "localhost",
    "puerto": 3306,
    "usuario": "root",
    "nombre": "unipaz_db",
    "pool": {
      "minConnections": 2,
      "maxConnections": 10
    }
  },
  "idioma": {
    "defecto": "es",
    "soportados": ["es", "en", "pt"],
    
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\data\logros.json`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```json

```

------------------------------------------------------------

#### `static\data\materias.json`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```json

```

------------------------------------------------------------

### JAVASCRIPT (15 archivos)

#### `static\js\analytics.js`
- **Líneas:** 164
- **Tamaño:** 4329 bytes

**Contenido:**
```js
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
```

------------------------------------------------------------

#### `static\js\api-config.js`
- **Líneas:** 122
- **Tamaño:** 3548 bytes

**Contenido:**
```js
// api-config.js - Configuración centralizada de API

const API_CONFIG = {
    // Base URL
    BASE_URL: 'http://localhost:5000',
    API_URL: 'http://localhost:5000/api',
    
    // Endpoints
    ENDPOINTS: {
        // Autenticación
        LOGIN: '/login',
        REGISTER: '/register',
        LOGOUT: '/logout',
        REFRESH_TOKEN: '/refresh-token',
        
        // Usuarios
        USUARIOS: '/usuarios',
        USUARIO_ID: (id) => `/usuarios/${id}`,
        USUARIO_PERFIL: (id) => `/usuarios/${id}/perfil`,
        USUARIO_ESTADISTICAS: (id) => `/usuarios/${id}/estadisticas`,
        USUARIO_HISTORIAL: (id) => `/usuarios/${id}/historial`,
        
        // Rankings
        RANKING_RACHA_GLOBAL: '/rankings/global/racha',
        RANKING_PORCENTAJE_GLOBAL: '/rankings/global/porcentaje',
        RANKING_MATERIA_RACHA: (id) => `/rankings/materia/${id}/racha`,
        RANKING_MATERIA_PORCENTAJE: (id) => `/rankings/materia/${id}/porcentaje`,
        
        // Materias
        MATERIAS: '/materias',
        MATERIA_ID: (id) => `/materias/${id}`,
        
        // Preguntas
        PREGUNTAS: (materiaId) => `/preguntas/${materiaId}`,
        SIGUIENTE_PREGUNTA: '/quiz/siguiente',
        
        // Quiz
        QUIZ_RESPONDER: '/quiz/responder',
        
        // Carreras
        CARRERAS: '/carreras',
        
        // Concursos
        CONCURSOS_ACTIVOS: '/concursos/activos',
        CONCURSO_ID: (id) => `/concursos/${id}`,
        CONCURSO_BRACKET: (id) => `/concursos/${id}/bracket`,
        CONCURSO_INSCRIBIRSE: (id) => `/concursos/${id}/inscribirse`,
        
        // Logros
        LOGROS_USUARIO: (id) => `/logros/usuario/${id}`,
        LOGRO_VERIFICAR: (id) => `/logros/verificar/${id}`,
        
        // Health
        HEALTH: '/health'
    },
    
    // Timeouts
    TIMEOUT: 30000,
    RETRY_ATTEMPTS: 3,
    RETRY_DELAY: 1000,
    
    // Headers por defecto
    HEADERS: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
    
    // Status codes
    STATUS_CODES: {
        OK: 200,
        CREATED: 201,
        BAD_REQUEST: 400,
        UNAUTHORIZED: 401,
        FORBIDDEN: 403,
        NOT_FOUND: 404,
        CONFLICT: 409,
        SERVER_ERROR: 500
    }
};

/**
 * Obtener URL completa del endpoint
 */
function obtenerURLEndpoint(endpoint) {
    if (endpoint.startsWith('http')) return endpoint;
    return API_CONFIG.API_URL + endpoint;
}

/**
 * Realizar llamada a API con retry
 */
async function llamarAPI(endpoint, opciones = {}) {
    let intentos = 0;
    const maxIntentos = opciones.reintentos || API_CONFIG.RETRY_ATTEMPTS;
    
    while (intentos < maxIntentos) {
        try {
            const url = obtenerURLEndpoint(endpoint);
            const config = {
                ...opciones,
                headers: {
                    ...API_CONFIG.HEADERS,
                    ...opciones.headers
                }
            };
            
            const response = await fetch(url, config);
            return response;
        } catch (error) {
            intentos++;
            if (intentos >= maxIntentos) throw error;
            await new Promise(r => setTimeout(r, API_CONFIG.RETRY_DELAY));
        }
    }
}

// Exportar globalmente
window.API_CONFIG = API_CONFIG;
window.obtenerURLEndpoint = obtenerURLEndpoint;
window.llamarAPI = llamarAPI;

console.log('✅ api-config.js cargado');
```

------------------------------------------------------------

#### `static\js\auth.js`
- **Líneas:** 250
- **Tamaño:** 6552 bytes

**Contenido:**
```js
// auth.js - Autenticación y Sesión UNIPAZ

console.log('✅ auth.js cargado');

// ===== VARIABLES GLOBALES =====

let usuarioActual = null;
let tokenActual = null;

// ===== AUTENTICACIÓN =====

/**
 * Iniciar sesión
 */
async function iniciarSesion(email, password) {
    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            tokenActual = data.token;
            usuarioActual = data.usuario;
            
            // Guardar en localStorage
            localStorage.setItem('token', tokenActual);
            localStorage.setItem('usuario', JSON.stringify(usuarioActual));
            
            UNIPAZ.CONFIG.usuarioId = usuarioActual.id;
            
            console.log('✅ Sesión iniciada:', usuarioActual);
            UNIPAZ.mostrarNotificacion(`¡Bienvenido, ${usuarioActual.nombre}!`, 'success');
            
            return true;
        } else {
            UNIPAZ.mostrarNotificacion(data.error || 'Error en login', 'error');
        }
    } catch (error) {
        console.error('Error en iniciarSesion:', error);
        UNIPAZ.mostrarNotificacion('Error de conexión', 'error');
    }
    return false;
}

/**
 * Registrarse
 */
async function registrarse(datos) {
    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(datos)
        });

        const data = await response.json();

        if (response.ok) {
            UNIPAZ.mostrarNotificacion('¡Registro exitoso! Inicia sesión.', 'success');
            return true;
        } else {
            UNIPAZ.mostrarNotificacion(data.error || 'Error en registro', 'error');
        }
    } catch (error) {
        console.error('Error en registrarse:', error);
    }
    return false;
}

/**
 * Cerrar sesión
 */
async function cerrarSesion() {
    try {
        await fetch('/api/logout', { method: 'POST' });
        
        localStorage.removeItem('token');
        localStorage.removeItem('usuario');
        
        usuarioActual = null;
        tokenActual = null;
        
        UNIPAZ.mostrarNotificacion('Sesión cerrada', 'success');
        window.location.href = '/login';
    } catch (error) {
        console.error('Error cerrando sesión:', error);
    }
}

/**
 * Verificar si está autenticado
 */
function estaAutenticado() {
    tokenActual = localStorage.getItem('token');
    usuarioActual = JSON.parse(localStorage.getItem('usuario') || 'null');
    
    return !!tokenActual && !!usuarioActual;
}

/**
 * Obtener usuario actual
 */
function obtenerUsuarioActual() {
    if (!estaAutenticado()) {
        return null;
    }
    return usuarioActual;
}

/**
 * Obtener token
 */
function obtenerToken() {
    return localStorage.getItem('token');
}

/**
 * Renovar contraseña
 */
async function renovarContrasena(emailOrId, emailNuevo, contrasenaActual, contrasenaNueva) {
    try {
        const response = await fetch('/api/cambiar-contrasena', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${obtenerToken()}`
            },
            body: JSON.stringify({
                emailOrId,
                emailNuevo,
                contrasenaActual,
                contrasenaNueva
            })
        });

        const data = await response.json();

        if (response.ok) {
            UNIPAZ.mostrarNotificacion('Contraseña actualizada', 'success');
            return true;
        } else {
            UNIPAZ.mostrarNotificacion(data.error || 'Error al cambiar contraseña', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
    }
    return false;
}

/**
 * Recuperar contraseña
 */
async function recuperarContrasena(email) {
    try {
        const response = await fetch('/api/recuperar-contrasena', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email })
        });

        const data = await response.json();

        if (response.ok) {
            UNIPAZ.mostrarNotificacion('Revisa tu email para recuperar acceso', 'success');
            return true;
        } else {
            UNIPAZ.mostrarNotificacion(data.error || 'Error', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
    }
    return false;
}

/**
 * Verificar permisos (Admin)
 */
function esAdmin() {
    return usuarioActual && usuarioActual.rol === 'admin';
}

/**
 * Verificar permisos (Profesor)
 */
function esProfesor() {
    return usuarioActual && usuarioActual.rol === 'profesor';
}

/**
 * Redireccionar si no autenticado
 */
function protegerRuta() {
    if (!estaAutenticado()) 
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\js\concursos.js`
- **Líneas:** 338
- **Tamaño:** 9856 bytes

**Contenido:**
```js
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
        const resultado = await UNIPAZ.responderConcurso(concursoActual, respuesta
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\js\export-data.js`
- **Líneas:** 101
- **Tamaño:** 3475 bytes

**Contenido:**
```js
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
```

------------------------------------------------------------

#### `static\js\localStorage-helper.js`
- **Líneas:** 259
- **Tamaño:** 6027 bytes

**Contenido:**
```js
// localStorage-helper.js - Gestor de localStorage UNIPAZ

console.log('✅ localStorage-helper.js cargado');

const STORAGE_KEYS = {
    // Autenticación
    TOKEN: 'unipaz_token',
    USUARIO: 'unipaz_usuario',
    
    // Preferencias
    TEMA: 'unipaz_tema',
    IDIOMA: 'unipaz_idioma',
    NOTIFICACIONES: 'unipaz_notificaciones',
    
    // Datos temporales
    MATERIA_SELECCIONADA: 'unipaz_materia',
    QUIZ_EN_PROGRESO: 'unipaz_quiz_progreso',
    ULTIMO_DUELO: 'unipaz_ultimo_duelo',
    
    // Caché
    CARRERAS_CACHE: 'unipaz_carreras_cache',
    MATERIAS_CACHE: 'unipaz_materias_cache',
    RANKINGS_CACHE: 'unipaz_rankings_cache'
};

/**
 * Guardar dato en localStorage
 */
function guardarDato(clave, valor, tipo = 'json') {
    try {
        if (tipo === 'json') {
            localStorage.setItem(clave, JSON.stringify(valor));
        } else {
            localStorage.setItem(clave, valor);
        }
        console.log(`✅ Guardado: ${clave}`);
    } catch (error) {
        console.error(`Error guardando ${clave}:`, error);
    }
}

/**
 * Obtener dato de localStorage
 */
function obtenerDato(clave, tipo = 'json') {
    try {
        const valor = localStorage.getItem(clave);
        if (!valor) return null;
        
        if (tipo === 'json') {
            return JSON.parse(valor);
        } else {
            return valor;
        }
    } catch (error) {
        console.error(`Error obteniendo ${clave}:`, error);
        return null;
    }
}

/**
 * Eliminar dato de localStorage
 */
function eliminarDato(clave) {
    try {
        localStorage.removeItem(clave);
        console.log(`✅ Eliminado: ${clave}`);
    } catch (error) {
        console.error(`Error eliminando ${clave}:`, error);
    }
}

/**
 * Limpiar todo el localStorage (CUIDADO)
 */
function limpiarTodo() {
    try {
        localStorage.clear();
        console.log('✅ localStorage limpiado');
    } catch (error) {
        console.error('Error limpiando localStorage:', error);
    }
}

/**
 * Guardar token
 */
function guardarToken(token) {
    guardarDato(STORAGE_KEYS.TOKEN, token, 'string');
}

/**
 * Obtener token
 */
function obtenerToken() {
    return obtenerDato(STORAGE_KEYS.TOKEN, 'string');
}

/**
 * Guardar usuario
 */
function guardarUsuario(usuario) {
    guardarDato(STORAGE_KEYS.USUARIO, usuario, 'json');
}

/**
 * Obtener usuario
 */
function obtenerUsuario() {
    return obtenerDato(STORAGE_KEYS.USUARIO, 'json');
}

/**
 * Verificar sesión activa
 */
function tieneSesion() {
    return !!obtenerToken() && !!obtenerUsuario();
}

/**
 * Cerrar sesión (eliminar datos de autenticación)
 */
function cerrarSesionLocal() {
    eliminarDato(STORAGE_KEYS.TOKEN);
    eliminarDato(STORAGE_KEYS.USUARIO);
    console.log('✅ Sesión cerrada en cliente');
}

/**
 * Guardar preferencias
 */
function guardarPreferencias(tema, idioma, notificaciones) {
    guardarDato(STORAGE_KEYS.TEMA, tema, 'string');
    guardarDato(STORAGE_KEYS.IDIOMA, idioma, 'string');
    guardarDato(STORAGE_KEYS.NOTIFICACIONES, notificaciones, 'string');
}

/**
 * Obtener preferencias
 */
function obtenerPreferencias() {
    return {
        tema: obtenerDato(STORAGE_KEYS.TEMA, 'string') || 'dark',
        idioma: obtenerDato(STORAGE_KEYS.IDIOMA, 'string') || 'es',
        notificaciones: obtenerDato(STORAGE_KEYS.NOTIFICACIONES, 'string') || 'true'
    };
}

/**
 * Guardar materia seleccionada
 */
function guardarMateriaSeleccionada(materiaId) {
    guardarDato(STORAGE_KEYS.MATERIA_SELECCIONADA, materiaId, 'string');
}

/**
 * Obtener materia seleccionada
 */
function obtenerMateriaSeleccionada() {
    const materia = obtenerDato(STORAGE_KEYS.MATERIA_SELECCIONADA, 'string');
    return materia ? parseInt(materia) : null;
}

/**
 * Guardar progreso del quiz
 */
function guardarProgresoQuiz(datos) {
    guardarDato(STORAGE_KEYS.QUIZ_EN_PROGRESO, datos, 'json');
}

/**
 * Obtener progreso del quiz
 */
function obtenerProgresoQuiz() {
    return obtenerDato(STORAGE_KEYS.QUIZ_EN_PROGRESO, 'json');
}

/**
 * Limpiar progreso del quiz
 */
function limpiarProgresoQuiz() {
    eliminarDato(STORAGE_KEYS.QUIZ_EN_PROGRESO);
}

/**
 * Guardar caché con expiración
 */
function guardarCacheConExpiracion(clave, valor, minutos = 30) {
    const data = {
        valor: valor,
        expiracion: Date.now() + (minutos * 60 * 1000)
    };
    guardarDato(clave, data, 'json');
}

/**
 * Obtener caché (si no está expirado)
 */
function obtenerCache(clave) {
    const data = obtenerDato(clave, 'json');
    if (!data) return null;
    
    if (Date.now() > data.expiracion) {
        eliminarDato(clave);
        return null;
    }
    
    return data.valor;
}

/**
 * Exportar todos los datos (para backup)
 */
function exportarDatos() {
    const datos = {};
    for (let i = 0; i < localStorage.length; i++) {
        const clave = localStorage.key(i);
        datos[clave] = localStorage.getItem(clave);
    }
    return datos;
}

/**
 * Importar datos (restore backup)
 */
function impor
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\js\logros.js`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```js

```

------------------------------------------------------------

#### `static\js\main.js`
- **Líneas:** 389
- **Tamaño:** 9634 bytes

**Contenido:**
```js
// main.js - JavaScript Principal UNIPAZ Quiz System

console.log('✅ Sistema de Exámenes UNIPAZ Cargado');

// ===== CONFIG GLOBAL =====
const CONFIG = {
    apiUrl: 'http://localhost:5000/api',
    usuarioId: 1,
    modo: 'normal'
};

// ===== UTILIDADES =====

/**
 * Realizar petición fetch a la API
 */
async function apiCall(endpoint, options = {}) {
    const url = `${CONFIG.apiUrl}${endpoint}`;
    const config = {
        headers: {
            'Content-Type': 'application/json',
            ...options.headers
        },
        ...options
    };
    
    try {
        const response = await fetch(url, config);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        mostrarNotificacion('Error en la conexión', 'error');
        return null;
    }
}

/**
 * Mostrar notificación al usuario
 */
function mostrarNotificacion(mensaje, tipo = 'info', duracion = 3000) {
    const notificacion = document.createElement('div');
    notificacion.className = `notificacion notificacion-${tipo}`;
    notificacion.textContent = mensaje;
    notificacion.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        background: ${tipo === 'success' ? '#43e97b' : tipo === 'error' ? '#f5576c' : '#667eea'};
        color: white;
        border-radius: 8px;
        font-weight: 600;
        z-index: 10000;
        animation: slideInRight 0.3s ease;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    `;
    
    document.body.appendChild(notificacion);
    
    setTimeout(() => {
        notificacion.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => notificacion.remove(), 300);
    }, duracion);
}

/**
 * Formatear número a formato legible
 */
function formatearNumero(num) {
    return new Intl.NumberFormat('es-CO').format(num);
}

/**
 * Formatear fecha
 */
function formatearFecha(fecha) {
    return new Date(fecha).toLocaleDateString('es-CO');
}

/**
 * Guardar en localStorage
 */
function guardarLocal(clave, valor) {
    localStorage.setItem(clave, JSON.stringify(valor));
}

/**
 * Obtener de localStorage
 */
function obtenerLocal(clave) {
    const valor = localStorage.getItem(clave);
    return valor ? JSON.parse(valor) : null;
}

// ===== AUTENTICACIÓN =====

/**
 * Verificar sesión del usuario
 */
function verificarSesion() {
    const usuario = obtenerLocal('usuario');
    if (!usuario) {
        console.warn('No hay sesión activa');
        return false;
    }
    CONFIG.usuarioId = usuario.id;
    return true;
}

/**
 * Cerrar sesión
 */
function cerrarSesion() {
    localStorage.removeItem('usuario');
    localStorage.removeItem('token');
    window.location.href = '/login';
}

// ===== RANKINGS =====

/**
 * Cargar rankings globales
 */
async function cargarRankings() {
    console.log('Cargando rankings...');
    
    try {
        const [rachas, porcentajes] = await Promise.all([
            apiCall('/rankings/global/racha'),
            apiCall('/rankings/global/porcentaje')
        ]);
        
        if (rachas && porcentajes) {
            console.log('Rankings cargados:', { rachas, porcentajes });
            return { rachas, porcentajes };
        }
    } catch (error) {
        console.error('Error cargando rankings:', error);
    }
    return null;
}

/**
 * Cargar rankings por materia
 */
async function cargarRankingsPorMateria(materiaId) {
    console.log(`Cargando rankings para materia ${materiaId}...`);
    
    try {
        const [rachas, porcentajes] = await Promise.all([
            apiCall(`/rankings/materia/${materiaId}/racha`),
            apiCall(`/rankings/materia/${materiaId}/porcentaje`)
        ]);
        
        return { rachas, porcentajes };
    } catch (error) {
        console.error('Error cargando rankings por materia:', error);
    }
    return null;
}

// ===== CONCURSOS =====

/**
 * Cargar concursos activos
 */
async function cargarConcursosActivos() {
    console.log('Cargando concursos activos...');
    const data = await apiCall('/concursos/activos');
    return data;
}

/**
 * Inscribir en concurso
 */
async function inscribirConcurso(concursoId) {
    console.log(`Inscribiendo en concurso ${concursoId}...`);
    
    const data = await apiCall(`/concursos/${concursoId}/inscribirse`, {
        method: 'POST',
        body: JSON.stringify({
            usuario_id: CONFIG.usuarioId
        })
    });
    
    if (data) {
        mostrarNotificacion('¡Inscripción exitosa!', 'success');
        return true;
    }
    return false;
}

/**
 * Obtener bracket de concurso
 */
async function obtenerBracket(concursoId) {
    console.log(`Obteniendo bracket del concurso ${concursoId}...`);
    const data = await apiCall(`/concursos/${concursoId}/bracket`);
    return data;
}

/**
 * Responder pregunta en concurso
 */
async function responderConcurso(conc
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\js\materias.js`
- **Líneas:** 133
- **Tamaño:** 3551 bytes

**Contenido:**
```js
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
```

------------------------------------------------------------

#### `static\js\math-panel.js`
- **Líneas:** 370
- **Tamaño:** 13286 bytes

**Contenido:**
```js
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

 
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\js\notifications.js`
- **Líneas:** 178
- **Tamaño:** 4873 bytes

**Contenido:**
```js
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
```

------------------------------------------------------------

#### `static\js\quiz.js`
- **Líneas:** 324
- **Tamaño:** 9335 bytes

**Contenido:**
```js
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
        UNIPAZ.mostrarNotificacion('✅ ¡Correcto!', 
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\js\ranking.js`
- **Líneas:** 320
- **Tamaño:** 8996 bytes

**Contenido:**
```js
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

    tabla.inner
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\js\search.js`
- **Líneas:** 230
- **Tamaño:** 6603 bytes

**Contenido:**
```js
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
         
[... contenido truncado ...]
```

------------------------------------------------------------

#### `static\js\utils.js`
- **Líneas:** 473
- **Tamaño:** 9925 bytes

**Contenido:**
```js
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
function truncarTexto(texto, lon
[... contenido truncado ...]
```

------------------------------------------------------------

### MARKDOWN (4 archivos)

#### `README.md`
- **Líneas:** 271
- **Tamaño:** 6261 bytes

**Contenido:**
```md
# 🎓 Sistema de Exámenes UNIPAZ

## Descripción

Sistema completo de exámenes y evaluaciones académicas para la Universidad Nacional de la Paz (UNIPAZ) con sistema de rankings, concursos por eliminación, logros desbloqueables y gamificación.

## 🚀 Características Principales

### 📊 Rankings
- **Top 10 Mejores Rachas** - Global y por materia
- **Top 10 Porcentaje de Éxito** - Global y por materia
- Actualización en tiempo real
- Medallas animadas (Oro, Plata, Bronce)

### ⚔️ Concursos
- Sistema de **eliminación por rondas**
- Torneos 1 vs 1
- Árbol de bracket visual
- Eliminación por respuesta incorrecta o tiempo agotado
- Premios para los 3 primeros lugares

### 🎖️ Sistema de Logros
- Logros desbloqueables
- Badges animados
- Notificaciones al desbloquear
- Categorías: Principiante, Racha, Maestría, Desafíos

### 🎮 Modos de Juego
- **Normal**: 100 preguntas por nivel, progresión gradual
- **Hardcore**: Selección de nivel, reinicio al fallar
- **Pesadilla**: 10 niveles consecutivos sin errores

### ⚡ Powerups
- Escudo (protección contra 1 error)
- Pista (ver respuesta o eliminar 2 opciones)
- Tiempo Extra (+30 segundos)
- Doble Puntos (x2 en siguiente pregunta)
- Ayuda (destacar opción más probable)

### 👤 Perfil de Usuario
- Dashboard personalizado
- Estadísticas detalladas
- Nivel y experiencia (XP)
- Racha actual
- Historial de logros

## 🛠️ Tecnologías

### Backend
- **Python 3.9+**
- **Flask** (Framework web)
- **SQLAlchemy** (ORM)
- **Flask-CORS** (APIs)
- **MySQL** (Base de datos)

### Frontend
- **HTML5**
- **CSS3** (Animaciones modernas)
- **JavaScript** (ES6+)
- **Fetch API** (Comunicación con backend)

## 📁 Estructura del Proyecto

```
unipaz-quiz-system/
├── backend/
│   ├── routes/          # Endpoints API
│   ├── models/          # Modelos BD
│   ├── services/        # Lógica de negocio
│   └── config/          # Configuración
├── templates/           # HTML
├── static/
│   ├── css/            # Estilos
│   ├── js/             # Scripts
│   └── images/         # Recursos
├── database/           # SQL schemas
├── tests/              # Tests unitarios
└── docs/               # Documentación
```

## 🔧 Instalación

### 1. Clonar repositorio
```bash
git clone https://github.com/unipaz/quiz-system.git
cd unipaz-quiz-system
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos
```bash
# Crear base de datos
mysql -u root -p -e "CREATE DATABASE unipaz_db;"

# Importar schema
mysql -u root -p unipaz_db < database/schema.sql

# Importar datos de prueba
mysql -u root -p unipaz_db < database/seeds.sql
```

### 5. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

### 6. Ejecutar aplicación
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 🌐 Endpoints API

### Rankings
```
GET /api/rankings/global/racha          # Top 10 rachas global
GET /api/rankings/global/porcentaje     # Top 10 % éxito global
GET /api/rankings/materia/:id/racha     # Top 10 rachas por materia
GET /api/rankings/materia/:id/porcentaje # Top 10 % éxito por materia
```

### Concursos
```
GET  /api/concursos/activos             # Concursos en vivo
GET  /api/concursos/:id/bracket         # Árbol del torneo
POST /api/concursos/:id/inscribirse     # Inscribirse
POST /api/concursos/:id/responder       # Enviar respuesta
GET  /api/concursos/:id/estado          # Estado actual
```

### Logros
```
GET  /api/logros/usuario/:id            # Logros del usuario
POST /api/logros/verificar/:id          # Verificar logro
```

### Usuario
```
GET  /api/usuario/:id/perfil            # Datos del perfil
PUT  /api/usuario/:id/actualizar        # Actualizar perfil
GET  /api/usuario/:id/estadisticas      # Estadísticas
```

### Quiz
```
POST /api/quiz/respuesta                # Enviar respuesta
GET  /api/quiz/siguiente-pregunta       # Obtener siguiente
```

## 📊 Base de Datos

### Tablas Principales
- `usuarios` - Información de usuarios
- `rankings` - Rankings globales y por materia
- `concursos` - Torneos por eliminación
- `logros` - Logros desbloqueables
- `preguntas` - Banco de preguntas
- `examenes` - Exámenes creados
- `respuestas` - Respuestas de usuarios
- `powerups` - Powerups disponibles

## 🎨 Características de UI

### Diseño
- ✅ Bordes cuadrados (8px)
- ✅ Gradientes modernos
- ✅ Colores por carrera
- ✅ Animaciones suaves
- ✅ Responsive design
- ✅ Dark theme

### Animaciones
- Fade-in al cargar
- Slide-up en cards
- Pulse en badges
- Hover effects
- Confetti al ganar
- Notificaciones toast

## 👥 Roles de Usuario

### Estudiante
- Responder quizzes
- Ver rankings
- Participar en concursos
- Desbloquear logros
- Ver perfil

### Profesor
- Crear exámenes
- Configurar powerups
- Ver reportes
- Gestionar preguntas

### Admin
- Gestión completa
- Crear concursos
- Ver estadístic
[... contenido truncado ...]
```

------------------------------------------------------------

#### `docs\API.md`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```md

```

------------------------------------------------------------

#### `docs\DATABASE.md`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```md

```

------------------------------------------------------------

#### `docs\SETUP.md`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```md

```

------------------------------------------------------------

### OTRO (1 archivos)

#### `env`
- **Líneas:** 68
- **Tamaño:** 1366 bytes

**Contenido:**
```
# ===== ENTORNO =====
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_APP=app.py

# ===== BASE DE DATOS =====
# Nombre de la BD: unipaz_db
# Usuario: root
# Contraseña: 1606
# Host: localhost
# Puerto: 3306

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=1606
DB_NAME=unipaz_db
DB_CHARSET=utf8mb4

# URL de conexión SQLAlchemy
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:1606@localhost:3306/unipaz_db
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_ECHO=True

# ===== JWT (Tokens) =====
JWT_SECRET_KEY=unipaz_secret_key_2025_super_segura_no_cambiar
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# ===== API =====
API_PORT=5000
API_HOST=0.0.0.0
API_DEBUG=True

# ===== CORS =====
CORS_ORIGINS=*
CORS_ALLOW_HEADERS=Content-Type,Authorization

# ===== EMAIL (Opcional) =====
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=tu_email@gmail.com
MAIL_PASSWORD=tu_contraseña_app
MAIL_DEFAULT_SENDER=noreply@unipaz.edu

# ===== ZONA HORARIA =====
TIMEZONE=America/Bogota

# ===== LOGGING =====
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# ===== CACHE =====
CACHE_TYPE=simple
CACHE_DEFAULT_TIMEOUT=300

# ===== SEGURIDAD =====
SECRET_KEY=unipaz_secret_key_2025
SESSION_COOKIE_SECURE=False
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Lax

# ===== DESARROLLO =====
TESTING=False
PROPAGATE_EXCEPTIONS=True
PRESERVE_CONTEXT_ON_EXCEPTION=None

```

------------------------------------------------------------

### PYTHON (15 archivos)

#### `app.py`
- **Líneas:** 646
- **Tamaño:** 20127 bytes

**Documentación:**
- **Módulo:**
  ```
  UNIPAZ Quiz System - Backend Flask Completo

Conecta a: unipaz_db | Usuario: root | Contraseña: 1606

CON AUTENTICACIÓN, LOGIN Y REGISTRO FUNCIONALES

ACTUALIZADO: 2025-11-10 - RUTAS CORREGIDAS + IMPORT BACKEND ROUTES
  ```
- **Clase: Carrera:**
  ```
  Hashear contraseña
  ```
- **Función: verificar_password:**
  ```
  Verificar contraseña
  ```
- **Función: index:**
  ```
  Home page
  ```
- **Función: login:**
  ```
  Login page
  ```
- **Función: registro:**
  ```
  Registro page
  ```
- **Función: quiz:**
  ```
  Quiz page
  ```
- **Función: rankings:**
  ```
  Rankings page
  ```
- **Función: concursos:**
  ```
  Concursos page
  ```
- **Función: dashboard:**
  ```
  Dashboard page
  ```
- **Función: crear_examen_page:**
  ```
  Página para crear examen
  ```
- **Función: unirse_examen_page:**
  ```
  Página para unirse a examen
  ```
- **Función: debug_examen:**
  ```
  Página de debug para unirse a examen
  ```
- **Función: ver_examen:**
  ```
  Página para responder examen
  ```
- **Función: api_login:**
  ```
  Endpoint para login
  ```
- **Función: api_register:**
  ```
  Endpoint para registro
  ```
- **Función: get_carreras:**
  ```
  Obtener todas las carreras
  ```
- **Función: get_materias:**
  ```
  Obtener todas las materias
  ```
- **Función: get_materias_por_carrera:**
  ```
  Obtener materias de una carrera específica - CORREGIDO CON PARAMETRO
  ```
- **Función: get_preguntas:**
  ```
  Obtener preguntas de una materia - CORREGIDO CON PARAMETRO
  ```
- **Función: crear_examen_api:**
  ```
  Crear un examen
  ```
- **Función: agregar_pregunta:**
  ```
  Agregar una pregunta a un examen
  ```
- **Función: obtener_preguntas_examen:**
  ```
  Obtener preguntas de un examen
  ```
- **Función: buscar_examen_codigo:**
  ```
  Buscar examen por código de acceso
  ```
- **Función: obtener_examen:**
  ```
  Obtener detalles de un examen
  ```
- **Función: rankings_racha:**
  ```
  Top 10 mejores rachas
  ```
- **Función: health:**
  ```
  Verificar conexión a BD
  ```

**Imports:**
  - `import os`
  - `import hashlib`
  - `import secrets`
  - `import sys`
  - `from datetime import timedelta`
  - `from pathlib import Path`
  - `from flask import Flask, render_template, request, jsonify`
  - `from flask_sqlalchemy import SQLAlchemy`
  - `from flask_cors import CORS`
  - `from dotenv import load_dotenv`
  - `from routes import registrar_rutas`

**Contenido:**
```py
"""

UNIPAZ Quiz System - Backend Flask Completo

Conecta a: unipaz_db | Usuario: root | Contraseña: 1606

CON AUTENTICACIÓN, LOGIN Y REGISTRO FUNCIONALES

ACTUALIZADO: 2025-11-10 - RUTAS CORREGIDAS + IMPORT BACKEND ROUTES

"""

import os
import hashlib
import secrets
import sys
from datetime import timedelta
from pathlib import Path
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv


# Cargar variables de entorno
load_dotenv()


# ===== INICIALIZAR FLASK =====
app = Flask(__name__,
    template_folder='templates',
    static_folder='static'
)


# ===== CONFIGURACIÓN =====
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1606@localhost:3306/unipaz_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['JSON_SORT_KEYS'] = False


# ===== INICIALIZAR EXTENSIONES =====
db = SQLAlchemy(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})


# ===== MODELOS =====


class Carrera(db.Model):
    __tablename__ = 'carreras'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    icono = db.Column(db.String(50))
    color = db.Column(db.String(7))


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    carrera_id = db.Column(db.Integer, db.ForeignKey('carreras.id'))
    racha_actual = db.Column(db.Integer, default=0)
    racha_maxima = db.Column(db.Integer, default=0)
    total_puntos = db.Column(db.Integer, default=0)
    preguntas_correctas = db.Column(db.Integer, default=0)
    preguntas_totales = db.Column(db.Integer, default=0)


class Materia(db.Model):
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    carrera_id = db.Column(db.Integer, db.ForeignKey('carreras.id'), nullable=False)
    semestre = db.Column(db.Integer)
    profesor = db.Column(db.String(150))
    descripcion = db.Column(db.Text)


class Pregunta(db.Model):
    __tablename__ = 'preguntas'
    id = db.Column(db.Integer, primary_key=True)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    opcion_a = db.Column(db.String(500))
    opcion_b = db.Column(db.String(500))
    opcion_c = db.Column(db.String(500))
    opcion_d = db.Column(db.String(500))
    respuesta_correcta = db.Column(db.String(1))
    dificultad = db.Column(db.String(20), default='medio')
    activo = db.Column(db.Boolean, default=True)


class Examen(db.Model):
    __tablename__ = 'examenes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    creado_por = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    descripcion = db.Column(db.Text)
    duracion_minutos = db.Column(db.Integer, default=60)
    contraseña = db.Column(db.String(100))
    codigo_acceso = db.Column(db.String(50), unique=True, nullable=True)
    permitir_repaso = db.Column(db.Boolean, default=True)
    mostrar_puntaje_inmediato = db.Column(db.Boolean, default=True)
    permitir_volver_atras = db.Column(db.Boolean, default=True)
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=db.func.now())


# ===== TABLA INTERMEDIA PARA EXAMEN-PREGUNTA =====
class ExamenPregunta(db.Model):
    __tablename__ = 'examen_preguntas'
    id = db.Column(db.Integer, primary_key=True)
    examen_id = db.Column(db.Integer, db.ForeignKey('examenes.id'), nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('preguntas.id'), nullable=False)
    orden = db.Column(db.Integer, default=0)
    puntos = db.Column(db.Integer, default=1)


# ===== FUNCIONES AUXILIARES =====


def hashear_password(password):
    """Hashear contraseña"""
    return hashlib.sha256(password.encode()).hexdigest()


def verificar_password(password, password_hash):
    """Verificar contraseña"""
    return hashear_password(password) == password_hash


# ===== RUTAS FRONTEND =====


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/login')
def login():
    """Login page"""
    return render_template('login.html')


@app.route('/registro')
def registro():
    """Registro page"""
    return render_template('registro.html')


@app.route('/quiz')
def quiz():
    """Quiz page"""
    return render_template('quiz.html')


@app.route('/rankings')
def rankings():
    """Rankings page"""
    return render_template('rankings.html')


@app.route('/conc
[... contenido truncado ...]
```

------------------------------------------------------------

#### `backend\models\__init__.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `backend\models\concurso.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `backend\models\ranking.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `backend\models\usuario.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `backend\routes.py`
- **Líneas:** 511
- **Tamaño:** 16303 bytes

**Documentación:**
- **Función: obtener_materias:**
  ```
  Top 10 mejores rachas global
  ```
- **Función: ranking_porcentaje_global:**
  ```
  Top 10 mejor porcentaje de éxito global
  ```
- **Función: ranking_racha_materia:**
  ```
  Top 10 rachas por materia
  ```
- **Función: get_preguntas:**
  ```
  Obtener preguntas de una materia
  ```
- **Función: responder_pregunta:**
  ```
  Registrar respuesta de usuario
  ```
- **Función: siguiente_pregunta:**
  ```
  Obtener siguiente pregunta aleatoria
  ```
- **Función: estadisticas_usuario:**
  ```
  Obtener estadísticas del usuario
  ```
- **Función: historial_usuario:**
  ```
  Obtener historial de respuestas
  ```
- **Función: salud_api:**
  ```
  Endpoint de salud de la API
  ```
- **Función: registrar_rutas:**
  ```
  Función para registrar todos los blueprints en app.py
  ```

**Imports:**
  - `from flask import Blueprint, request, jsonify`
  - `from datetime import datetime, timedelta`
  - `from app import db`
  - `import random`
  - `import string`
  - `from app import Materia`
  - `from app import Examen`
  - `from app import Pregunta, Examen, ExamenPregunta`
  - `from app import Examen`
  - `from app import Pregunta, ExamenPregunta`
  - `from app import Usuario`
  - `from app import Usuario`
  - `from app import Usuario, Ranking`
  - `from app import Pregunta`
  - `from app import Respuesta, Pregunta, Usuario`
  - `from app import Pregunta`
  - `from app import Usuario, Respuesta`
  - `from app import Respuesta, Pregunta`

**Contenido:**
```py
# backend/routes.py - Rutas del Backend Flask COMPLETO Y CORREGIDO

from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from app import db
import random
import string


# ========== BLUEPRINTS ==========


rankigns_bp = Blueprint('rankings', __name__, url_prefix='/api/rankings')
quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quiz')
usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/api/usuarios')
api_bp = Blueprint('api', __name__, url_prefix='/api')  # Para examenes


# ========== MATERIAS ==========


@api_bp.route('/materias', methods=['GET'])
def obtener_materias():
    try:
        from app import Materia
        materias = Materia.query.filter_by(activo=True).order_by(Materia.nombre).all()
        return jsonify([{'id': m.id, 'nombre': m.nombre} for m in materias]), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ========== CREAR EXAMEN ==========


@api_bp.route('/examenes/crear', methods=['POST'])
def crear_examen():
    data = request.get_json()
    
    try:
        from app import Examen
        
        # Generar código de acceso
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        
        # Crear examen
        examen = Examen(
            materia_id=data['materia_id'],
            nombre=data['nombre'],
            duracion_minutos=data['duracion_minutos'],
            contraseña=data.get('contraseña'),
            codigo_acceso=codigo,
            activo=True
        )
        
        db.session.add(examen)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'examen_id': examen.id,
            'codigo_acceso': codigo
        }), 200
    except Exception as e:
        db.session.rollback()
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ========== CREAR PREGUNTA ==========


@api_bp.route('/examenes/<int:examen_id>/preguntas', methods=['POST'])
def crear_pregunta(examen_id):
    data = request.get_json()
    
    try:
        from app import Pregunta, Examen, ExamenPregunta
        
        # Validar que el examen exista
        examen = Examen.query.get(examen_id)
        if not examen:
            return jsonify({'error': 'Examen no encontrado'}), 404
        
        # 1. Crear la pregunta en tabla preguntas
        # IMPORTANTE: usar materia_id del payload
        pregunta = Pregunta(
            materia_id=data['materia_id'],
            texto=data['texto'],
            opcion_a=data['opcion_a'],
            opcion_b=data['opcion_b'],
            opcion_c=data['opcion_c'],
            opcion_d=data['opcion_d'],
            respuesta_correcta=data['respuesta_correcta'],
            activo=True
        )
        
        db.session.add(pregunta)
        db.session.flush()  # Para obtener el ID sin hacer commit
        
        # 2. Asociar pregunta al examen en tabla examen_preguntas
        examen_pregunta = ExamenPregunta(
            examen_id=examen_id,
            pregunta_id=pregunta.id,
            orden=0,
            puntos=1
        )
        
        db.session.add(examen_pregunta)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'pregunta_id': pregunta.id,
            'examen_id': examen_id
        }), 200
    except Exception as e:
        db.session.rollback()
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ========== OBTENER EXAMEN ==========


@api_bp.route('/examenes/<int:examen_id>', methods=['GET'])
def obtener_examen(examen_id):
    try:
        from app import Examen
        
        examen = Examen.query.get(examen_id)
        if not examen:
            return jsonify({'error': 'Examen no encontrado'}), 404
        
        return jsonify({
            'id': examen.id,
            'materia_id': examen.materia_id,
            'nombre': examen.nombre,
            'duracion_minutos': examen.duracion_minutos,
            'codigo_acceso': examen.codigo_acceso,
            'activo': examen.activo
        }), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500



# ========== OBTENER PREGUNTAS DEL EXAMEN ==========


@api_bp.route('/examenes/<int:examen_id>/preguntas', methods=['GET'])
def obtener_preguntas_examen(examen_id):
    try:
        from app import Pregunta, ExamenPregunta
        
        preguntas_rel = ExamenPregunta.query.filter_by(examen_id=examen_id)\
            .order_by(ExamenPregunta.orden).all()
        
        resultado = []
        for rel in preguntas_rel:
            p = rel.pregunta
            resultado.append({
                'id': p.id,
                'texto': p.texto,
                'opcion_a': p.opcion_a,
                'opcion_b': p.opcion_b,
                'opcion_c': p.opcion_c,
                'opcion_d': p.opcion_d,
                'respuesta_correcta': p.r
[... contenido truncado ...]
```

------------------------------------------------------------

#### `backend\services\__init__.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `backend\services\concurso_service.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `backend\services\ranking_service.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `export_routes.py`
- **Líneas:** 350
- **Tamaño:** 13951 bytes

**Documentación:**
- **Módulo:**
  ```
  Generador de Documentación de Proyecto para IA
==============================================

Este script escanea tu proyecto y genera un archivo de documentación completo
que puedes proporcionar a una IA para que entienda todo el contexto del proyecto.

Uso:
    python generar_documentacion.py [ruta_proyecto]

Autor: Generado para asistencia de IA
Fecha: 2025-11-10
  ```
- **Clase: DocumentacionProyecto:**
  ```
  Clase principal para generar documentación del proyecto
  ```
- **Función: __init__:**
  ```
  Verifica si una ruta debe ser ignorada
  ```
- **Función: obtener_tipo_archivo:**
  ```
  Obtiene el tipo de archivo basado en su extensión
  ```
- **Función: leer_archivo_seguro:**
  ```
  Lee un archivo de forma segura manejando diferentes encodings
  ```
- **Función: extraer_docstrings_python:**
  ```
  Extrae docstrings de archivos Python
  ```
- **Función: analizar_archivo:**
  ```
  Analiza un archivo y extrae información relevante
  ```
- **Función: escanear_proyecto:**
  ```
  Escanea todo el proyecto y recopila información
  ```
- **Función: generar_estructura_arbol:**
  ```
  Genera una representación en árbol de la estructura del proyecto
  ```
- **Función: generar_documentacion:**
  ```
  Genera el archivo de documentación completo
  ```
- **Función: main:**
  ```
  Función principal
  ```

**Imports:**
  - `import os`
  - `import json`
  - `from datetime import datetime`
  - `from pathlib import Path`
  - `import re`
  - `import sys`

**Contenido:**
```py
"""
Generador de Documentación de Proyecto para IA
==============================================

Este script escanea tu proyecto y genera un archivo de documentación completo
que puedes proporcionar a una IA para que entienda todo el contexto del proyecto.

Uso:
    python generar_documentacion.py [ruta_proyecto]

Autor: Generado para asistencia de IA
Fecha: 2025-11-10
"""

import os
import json
from datetime import datetime
from pathlib import Path
import re

class DocumentacionProyecto:
    """Clase principal para generar documentación del proyecto"""

    def __init__(self, ruta_raiz="."):
        self.ruta_raiz = Path(ruta_raiz).resolve()
        self.archivos_procesados = []
        self.estructura_proyecto = {}
        self.estadisticas = {
            "total_archivos": 0,
            "total_lineas": 0,
            "archivos_python": 0,
            "archivos_js": 0,
            "archivos_html": 0,
            "archivos_css": 0,
            "otros_archivos": 0
        }

        # Archivos y directorios a ignorar
        self.ignorar = {
            '__pycache__', '.git', '.venv', 'venv', 'node_modules',
            '.pytest_cache', '.mypy_cache', 'dist', 'build', '*.pyc',
            '.DS_Store', '.env', '.idea', '.vscode', '*.egg-info'
        }

        # Extensiones de archivos a procesar
        self.extensiones_codigo = {
            '.py': 'Python',
            '.js': 'JavaScript', 
            '.html': 'HTML',
            '.css': 'CSS',
            '.json': 'JSON',
            '.md': 'Markdown',
            '.txt': 'Text',
            '.sql': 'SQL',
            '.yml': 'YAML',
            '.yaml': 'YAML',
            '.xml': 'XML',
            '.sh': 'Shell',
            '.bat': 'Batch'
        }

    def debe_ignorar(self, ruta):
        """Verifica si una ruta debe ser ignorada"""
        partes = Path(ruta).parts
        for parte in partes:
            if parte in self.ignorar or parte.startswith('.'):
                return True
        return False

    def obtener_tipo_archivo(self, extension):
        """Obtiene el tipo de archivo basado en su extensión"""
        return self.extensiones_codigo.get(extension, 'Otro')

    def leer_archivo_seguro(self, ruta_archivo):
        """Lee un archivo de forma segura manejando diferentes encodings"""
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']

        for encoding in encodings:
            try:
                with open(ruta_archivo, 'r', encoding=encoding) as f:
                    return f.read()
            except (UnicodeDecodeError, UnicodeError):
                continue
            except Exception as e:
                return f"[Error al leer archivo: {str(e)}]"

        return "[Archivo binario o no se pudo decodificar]"

    def extraer_docstrings_python(self, contenido):
        """Extrae docstrings de archivos Python"""
        docstrings = []

        # Buscar docstrings de módulo (al inicio del archivo)
        match_modulo = re.search(r'^"""(.+?)"""', contenido, re.DOTALL | re.MULTILINE)
        if match_modulo:
            docstrings.append(("Módulo", match_modulo.group(1).strip()))

        # Buscar docstrings de funciones y clases
        patron = r'(def|class)\s+([\w_]+).*?:\s*"""(.+?)"""'
        for match in re.finditer(patron, contenido, re.DOTALL):
            tipo = "Clase" if match.group(1) == "class" else "Función"
            nombre = match.group(2)
            docstring = match.group(3).strip()
            docstrings.append((f"{tipo}: {nombre}", docstring))

        return docstrings

    def analizar_archivo(self, ruta_archivo):
        """Analiza un archivo y extrae información relevante"""
        try:
            ruta = Path(ruta_archivo)
            extension = ruta.suffix
            tipo = self.obtener_tipo_archivo(extension)

            contenido = self.leer_archivo_seguro(ruta_archivo)
            lineas = contenido.split('\n')
            num_lineas = len(lineas)

            # Actualizar estadísticas
            self.estadisticas["total_archivos"] += 1
            self.estadisticas["total_lineas"] += num_lineas

            if extension == '.py':
                self.estadisticas["archivos_python"] += 1
            elif extension == '.js':
                self.estadisticas["archivos_js"] += 1
            elif extension == '.html':
                self.estadisticas["archivos_html"] += 1
            elif extension == '.css':
                self.estadisticas["archivos_css"] += 1
            else:
                self.estadisticas["otros_archivos"] += 1

            info_archivo = {
                "ruta_relativa": str(ruta.relative_to(self.ruta_raiz)),
                "tipo": tipo,
                "extension": extension,
                "lineas": num_lineas,
                "tamaño_bytes": ruta.stat().st_size,
                "contenido": contenido[:5000] if len(contenido) < 5000 else contenido[:5000] + "\n[... contenido truncado ...]"
            }

            # Extraer información e
[... contenido truncado ...]
```

------------------------------------------------------------

#### `init_db.py`
- **Líneas:** 294
- **Tamaño:** 9954 bytes

**Documentación:**
- **Módulo:**
  ```
  Script de Inicialización de Base de Datos UNIPAZ
================================================
Este script llena la base de datos con datos de prueba.

Uso:
    python init_db.py

Requiere:
    - Base de datos 'unipaz_db' creada
    - MySQL/MariaDB funcionando
    - Credenciales correctas en la configuración
  ```
- **Función: conectar_db:**
  ```
  Conecta a la base de datos MySQL
  ```
- **Función: crear_tablas:**
  ```
  Crea las tablas si no existen
  ```
- **Función: limpiar_datos:**
  ```
  Limpia datos existentes
  ```
- **Función: insertar_carreras:**
  ```
  Inserta las carreras
  ```
- **Función: insertar_materias:**
  ```
  Inserta las materias por carrera
  ```
- **Función: insertar_preguntas:**
  ```
  Inserta preguntas de ejemplo
  ```
- **Función: verificar_datos:**
  ```
  Verifica que los datos se insertaron correctamente
  ```
- **Función: main:**
  ```
  Función principal
  ```

**Imports:**
  - `import mysql.connector`
  - `from mysql.connector import Error`
  - `import sys`

**Contenido:**
```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Inicialización de Base de Datos UNIPAZ
================================================
Este script llena la base de datos con datos de prueba.

Uso:
    python init_db.py

Requiere:
    - Base de datos 'unipaz_db' creada
    - MySQL/MariaDB funcionando
    - Credenciales correctas en la configuración
"""

import mysql.connector
from mysql.connector import Error
import sys

# ========== CONFIGURACIÓN ==========
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Cambiar si tienes contraseña
    'database': 'unipaz_db',
    'charset': 'utf8mb4'
}

# ========== DATOS A INSERTAR ==========

CARRERAS = [
    (1, 'Ingeniería en Sistemas', 'Carrera de Ingeniería', '⚙️', '#667eea'),
    (2, 'Medicina', 'Carrera de Medicina', '🏥', '#ee5a6f'),
    (3, 'Derecho', 'Carrera de Derecho', '⚖️', '#ff9ff3'),
    (4, 'Administración de Empresas', 'Carrera de Administración', '📊', '#1dd1a1'),
]

MATERIAS_POR_CARRERA = {
    1: [  # Ingeniería
        ('Cálculo I', 1, 'Matemáticas básicas'),
        ('Programación I', 1, 'Introducción a programación'),
        ('Álgebra Lineal', 2, 'Matrices y vectores'),
        ('Estructura de Datos', 2, 'Tipos de datos avanzados'),
        ('Base de Datos', 3, 'SQL y BD relacionales'),
        ('Sistemas Operativos', 3, 'Conceptos de SO'),
        ('Redes de Computadores', 4, 'Networking'),
        ('Ingeniería de Software', 4, 'Desarrollo de software'),
    ],
    2: [  # Medicina
        ('Anatomía I', 1, 'Sistema óseo y muscular'),
        ('Biología Celular', 1, 'Células y tejidos'),
        ('Fisiología I', 2, 'Funcionamiento de órganos'),
        ('Bioquímica', 2, 'Procesos químicos'),
        ('Patología', 3, 'Estudio de enfermedades'),
        ('Farmacología', 3, 'Medicamentos'),
        ('Cirugía General', 4, 'Procedimientos quirúrgicos'),
        ('Pediatría', 4, 'Medicina infantil'),
    ],
    3: [  # Derecho
        ('Derecho Constitucional', 1, 'Leyes fundamentales'),
        ('Introducción al Derecho', 1, 'Conceptos básicos'),
        ('Derecho Penal', 2, 'Crímenes y sanciones'),
        ('Derecho Civil', 2, 'Derechos civiles'),
        ('Derecho Laboral', 3, 'Relaciones laborales'),
        ('Derecho Administrativo', 3, 'Administración pública'),
        ('Derecho Mercantil', 4, 'Derecho comercial'),
        ('Derecho Internacional', 4, 'Derecho entre naciones'),
    ],
    4: [  # Administración
        ('Contabilidad Financiera', 1, 'Registros contables'),
        ('Economía General', 1, 'Principios económicos'),
        ('Marketing', 2, 'Estrategias de mercado'),
        ('Administración General', 2, 'Gestión empresarial'),
        ('Recursos Humanos', 3, 'Gestión de personal'),
        ('Finanzas Empresariales', 3, 'Análisis financiero'),
        ('Emprendimiento', 4, 'Crear negocios'),
        ('Gestión Estratégica', 4, 'Planificación estratégica'),
    ],
}

PREGUNTAS_EJEMPLO = [
    {
        'materia_id': 1,
        'texto': '¿Cuál es la derivada de x²?',
        'dificultad': 'facil',
        'opciones': ['x', '2x', '2x²', 'x/2'],
        'respuesta': 'B'
    },
    {
        'materia_id': 1,
        'texto': '¿Cuál es el límite de 1/x cuando x tiende a 0?',
        'dificultad': 'medio',
        'opciones': ['0', '1', 'Infinito', 'No existe'],
        'respuesta': 'C'
    },
    {
        'materia_id': 2,
        'texto': '¿Cuál es la sintaxis correcta en Python?',
        'dificultad': 'facil',
        'opciones': ['print "Hola"', 'print("Hola")', 'PRINT Hola', 'echo Hola'],
        'respuesta': 'B'
    },
]

def conectar_db():
    """Conecta a la base de datos MySQL"""
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        if conexion.is_connected():
            print("✅ Conectado a la base de datos")
            return conexion
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        sys.exit(1)

def crear_tablas(conexion):
    """Crea las tablas si no existen"""
    cursor = conexion.cursor()
    
    # Crear tabla carreras
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carreras (
            id INT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL UNIQUE,
            subtitulo VARCHAR(100),
            icono VARCHAR(50),
            color VARCHAR(20),
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Crear tabla materias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            carrera_id INT NOT NULL,
            semestre INT,
            descripcion TEXT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (carrera_id) REFERENCES carreras(id),
            UNIQUE KEY unique_materia (nombre, carrera_id)
        )
    ''')
    
    # Crear tabla preguntas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS preguntas (
          
[... contenido truncado ...]
```

------------------------------------------------------------

#### `mega_generador_unipaz.py`
- **Líneas:** 404
- **Tamaño:** 21096 bytes

**Documentación:**
- **Módulo:**
  ```
  MEGA GENERADOR DE PREGUNTAS UNIPAZ
- Todas las materias de UNIPAZ Barrancabermeja (9 semestres cada carrera)
- Todas las carreras completas
- 100 preguntas por materia
- Respuestas VARIADAS (no siempre A)
- Contenido académico realista
  ```
- **Clase: GeneradorPreguntasVariadas:**
  ```
  Generar una pregunta variada de una materia específica
  ```
- **Función: insertar_todas_carreras_materias_preguntas:**
  ```
  MEGA INSERTAR: Carreras → Materias → Preguntas
  ```

**Imports:**
  - `import random`
  - `import mysql.connector`
  - `from datetime import datetime`

**Contenido:**
```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MEGA GENERADOR DE PREGUNTAS UNIPAZ
- Todas las materias de UNIPAZ Barrancabermeja (9 semestres cada carrera)
- Todas las carreras completas
- 100 preguntas por materia
- Respuestas VARIADAS (no siempre A)
- Contenido académico realista
"""

import random
import mysql.connector
from datetime import datetime

# ============================================================
# CONFIGURACIÓN BD
# ============================================================

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1606',
    'database': 'unipaz_db'
}

# ============================================================
# TODAS LAS CARRERAS UNIPAZ REALES
# ============================================================

CARRERAS_COMPLETAS = {
    'Ingeniería en Sistemas': {
        'icono': '⚙️',
        'color': '#667eea',
        'materias': {
            1: ['Matemáticas I', 'Fundamentos de Programación', 'Lógica Matemática'],
            2: ['Cálculo II', 'Programación Orientada a Objetos', 'Estructuras Discretas'],
            3: ['Álgebra Lineal', 'Estructuras de Datos', 'Base de Datos I'],
            4: ['Ecuaciones Diferenciales', 'Sistemas Operativos', 'Base de Datos II'],
            5: ['Probabilidad y Estadística', 'Redes de Computadores', 'Ingeniería de Software'],
            6: ['Cálculo Multivariado', 'Compiladores', 'Seguridad Informática'],
            7: ['Análisis Numérico', 'Programación Web', 'Administración de BD'],
            8: ['Programación Avanzada', 'Inteligencia Artificial', 'Cloud Computing'],
            9: ['Verificación de Software', 'Desarrollo Móvil', 'Proyecto de Grado']
        }
    },
    'Medicina': {
        'icono': '🏥',
        'color': '#ee5a6f',
        'materias': {
            1: ['Anatomía Humana I', 'Biología Celular', 'Química Biológica'],
            2: ['Anatomía Humana II', 'Fisiología I', 'Histología'],
            3: ['Bioquímica', 'Fisiología II', 'Farmacología I'],
            4: ['Fisiopatología I', 'Farmacología II', 'Microbiología Médica'],
            5: ['Fisiopatología II', 'Patología General', 'Parasitología'],
            6: ['Semiología', 'Medicina Interna I', 'Epidemiología'],
            7: ['Medicina Interna II', 'Cirugía General', 'Ginecología'],
            8: ['Pediatría', 'Psiquiatría', 'Oftalmología'],
            9: ['Medicina Legal', 'Internado Clínico', 'Trabajo de Grado']
        }
    },
    'Derecho': {
        'icono': '⚖️',
        'color': '#ff9ff3',
        'materias': {
            1: ['Introducción al Derecho', 'Derecho Constitucional I', 'Historia del Derecho'],
            2: ['Derecho Constitucional II', 'Derecho Penal I', 'Derecho Administrativo I'],
            3: ['Derecho Civil I', 'Derecho Penal II', 'Derechos Humanos'],
            4: ['Derecho Civil II', 'Procedimiento Civil I', 'Derecho Laboral I'],
            5: ['Derecho Civil III', 'Procedimiento Civil II', 'Derecho Laboral II'],
            6: ['Derecho Mercantil I', 'Derecho Laboral III', 'Derecho Administrativo II'],
            7: ['Derecho Mercantil II', 'Derecho Tributario', 'Derecho de Familia'],
            8: ['Derecho Penal III', 'Derecho Internacional', 'Práctica Jurídica'],
            9: ['Seminario de Tesis', 'Responsabilidad Civil', 'Trabajo de Grado']
        }
    },
    'Administración de Empresas': {
        'icono': '📊',
        'color': '#1dd1a1',
        'materias': {
            1: ['Administración General', 'Contabilidad I', 'Economía General'],
            2: ['Microeconomía', 'Contabilidad II', 'Administración de Recursos'],
            3: ['Macroeconomía', 'Contabilidad de Costos', 'Marketing I'],
            4: ['Finanzas I', 'Administración Financiera', 'Marketing II'],
            5: ['Finanzas II', 'Evaluación de Proyectos', 'Comportamiento Organizacional'],
            6: ['Auditoría', 'Gestión Estratégica I', 'Gestión de RRHH'],
            7: ['Administración Pública', 'Gestión Estratégica II', 'Emprendimiento'],
            8: ['Negocios Internacionales', 'Gestión de la Calidad', 'Logística'],
            9: ['Seminario de Investigación', 'Administración Ambiental', 'Trabajo de Grado']
        }
    },
    'Ingeniería Civil': {
        'icono': '🏗️',
        'color': '#4ecdc4',
        'materias': {
            1: ['Matemáticas I', 'Física I', 'Geometría Descriptiva'],
            2: ['Matemáticas II', 'Física II', 'Dibujo Técnico'],
            3: ['Cálculo Multivariado', 'Estática', 'Mecánica de Materiales'],
            4: ['Dinámica', 'Resistencia de Materiales I', 'Topografía'],
            5: ['Análisis Estructural I', 'Hormigón Armado I', 'Geotecnia I'],
            6: ['Análisis Estructural II', 'Hormigón Armado II', 'Geotecnia II'],
            7: ['Acero Estructural', 'Hidráulica', 'Vías y Transporte'],
            8: ['Concreto Presforzado', 'Alcantarillado', 'Gestos de Proyectos'],
            9: ['Puentes', 'Ingeniería Sanitaria', 'Trabajo de Grado']
     
[... contenido truncado ...]
```

------------------------------------------------------------

#### `tests\__init__.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `tests\test_concursos.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

#### `tests\test_rankings.py`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```py

```

------------------------------------------------------------

### SQL (4 archivos)

#### `database\migrations\001_initial.sql`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```sql

```

------------------------------------------------------------

#### `database\migrations\002_add_rankings.sql`
- **Líneas:** 1
- **Tamaño:** 0 bytes

**Contenido:**
```sql

```

------------------------------------------------------------

#### `database\schema.sql`
- **Líneas:** 326
- **Tamaño:** 12826 bytes

**Contenido:**
```sql
-- SCHEMA SQL - Sistema de Exámenes UNIPAZ
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS unipaz_db;
USE unipaz_db;

-- ==================== TABLAS PRINCIPALES ====================

-- Tabla: Carreras
CREATE TABLE IF NOT EXISTS carreras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    subtitulo VARCHAR(100),
    color VARCHAR(20) DEFAULT '#667eea',
    icono VARCHAR(50) DEFAULT '📚',
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Materias
CREATE TABLE IF NOT EXISTS materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    carrera_id INT NOT NULL,
    semestre INT,
    color VARCHAR(20),
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (carrera_id) REFERENCES carreras(id) ON DELETE CASCADE,
    UNIQUE KEY unique_materia_carrera (nombre, carrera_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(200) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    carrera_id INT,
    nivel INT DEFAULT 1,
    xp INT DEFAULT 0,
    racha_actual INT DEFAULT 0,
    racha_maxima INT DEFAULT 0,
    total_puntos INT DEFAULT 0,
    preguntas_correctas INT DEFAULT 0,
    preguntas_totales INT DEFAULT 0,
    avatar VARCHAR(200) DEFAULT 'default.png',
    rol VARCHAR(20) DEFAULT 'estudiante',
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultima_actividad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (carrera_id) REFERENCES carreras(id) ON DELETE SET NULL,
    INDEX idx_email (email),
    INDEX idx_racha (racha_actual),
    INDEX idx_puntos (total_puntos)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Rankings
CREATE TABLE IF NOT EXISTS rankings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    valor FLOAT NOT NULL,
    posicion INT NOT NULL,
    materia_id INT,
    periodo VARCHAR(20) DEFAULT 'global',
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (materia_id) REFERENCES materias(id) ON DELETE SET NULL,
    UNIQUE KEY unique_ranking (usuario_id, tipo, materia_id, periodo),
    INDEX idx_posicion (posicion),
    INDEX idx_tipo (tipo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Logros (Templates)
CREATE TABLE IF NOT EXISTS logros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    icono VARCHAR(50) DEFAULT '🏆',
    categoria VARCHAR(50),
    requisito_tipo VARCHAR(50),
    requisito_valor INT,
    puntos_reward INT DEFAULT 10,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Usuario Logros (Relación many-to-many)
CREATE TABLE IF NOT EXISTS usuario_logros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    logro_id INT NOT NULL,
    fecha_desbloqueo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (logro_id) REFERENCES logros(id) ON DELETE CASCADE,
    UNIQUE KEY unique_usuario_logro (usuario_id, logro_id),
    INDEX idx_usuario (usuario_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Preguntas
CREATE TABLE IF NOT EXISTS preguntas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto TEXT NOT NULL,
    materia_id INT NOT NULL,
    dificultad VARCHAR(20) DEFAULT 'medio',
    opcion_a VARCHAR(200),
    opcion_b VARCHAR(200),
    opcion_c VARCHAR(200),
    opcion_d VARCHAR(200),
    respuesta_correcta VARCHAR(1),
    explicacion TEXT,
    imagen_url VARCHAR(200),
    creado_por INT,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (materia_id) REFERENCES materias(id) ON DELETE CASCADE,
    FOREIGN KEY (creado_por) REFERENCES usuarios(id) ON DELETE SET NULL,
    INDEX idx_materia (materia_id),
    INDEX idx_dificultad (dificultad)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: Respuestas (Registro de respuestas del usuario)
CREATE TABLE IF NOT EXISTS respuestas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    pregunta_id INT NOT NULL,
    respuesta_dada VARCHAR(1),
    es_correcta BOOLEAN,
    tiempo_respuesta INT,
    modo VARCHAR(20),
    materia_id INT,
    fecha_respuesta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(id) ON DELETE CASCADE,
    FORE
[... contenido truncado ...]
```

------------------------------------------------------------

#### `database\seeds.sql`
- **Líneas:** 129
- **Tamaño:** 8458 bytes

**Contenido:**
```sql
-- ============================================================
-- SEED DATA PARA UNIPAZ QUIZ SYSTEM
-- Inserta datos de prueba para que funcione el flujo completo
-- ============================================================

USE unipaz_db;

-- ============================================================
-- 1. INSERTAR MATERIAS POR CARRERA
-- ============================================================

-- Ingeniería (carrera_id = 1)
INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion) VALUES
('Cálculo I', 1, 1, 'Dr. García', 'Fundamentos de cálculo diferencial'),
('Programación I', 1, 1, 'Ing. López', 'Introducción a la programación'),
('Álgebra Lineal', 1, 2, 'Dr. Martínez', 'Matrices y espacios vectoriales'),
('Estructura de Datos', 1, 2, 'Ing. Rodríguez', 'Listas, árboles y grafos'),
('Base de Datos', 1, 3, 'Ing. Pérez', 'SQL y diseño de BD');

-- Medicina (carrera_id = 2)
INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion) VALUES
('Anatomía I', 2, 1, 'Dr. Cortés', 'Sistema óseo y muscular'),
('Fisiología', 2, 2, 'Dra. Rivera', 'Funcionamiento de órganos'),
('Patología', 2, 3, 'Dr. Morales', 'Estudio de enfermedades'),
('Farmacología', 2, 4, 'Dra. Sánchez', 'Medicamentos y sus efectos'),
('Cirugía General', 2, 5, 'Dr. Jiménez', 'Procedimientos quirúrgicos');

-- Derecho (carrera_id = 3)
INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion) VALUES
('Derecho Constitucional', 3, 1, 'Dr. Ávila', 'Leyes fundamentales'),
('Derecho Penal', 3, 2, 'Dra. Gómez', 'Crímenes y sanciones'),
('Derecho Civil', 3, 3, 'Dr. Castillo', 'Derechos y obligaciones civiles'),
('Derecho Laboral', 3, 4, 'Dra. Torres', 'Relaciones laborales'),
('Derecho Administrativo', 3, 5, 'Dr. Vargas', 'Administración pública');

-- Administración (carrera_id = 4)
INSERT INTO materias (nombre, carrera_id, semestre, profesor, descripcion) VALUES
('Contabilidad Financiera', 4, 1, 'CPA López', 'Registros contables'),
('Marketing', 4, 2, 'Lic. Mendez', 'Estrategias de mercado'),
('Recursos Humanos', 4, 3, 'Dra. Silva', 'Gestión de personal'),
('Finanzas Empresariales', 4, 4, 'MBA García', 'Análisis financiero'),
('Emprendimiento', 4, 5, 'Ing. Ruiz', 'Crear tu propio negocio');

-- ============================================================
-- 2. INSERTAR PREGUNTAS DE PRUEBA (INGENIERÍA - CÁLCULO)
-- ============================================================

-- Matemáticas I - Carrera 1 (Ingeniería)
INSERT INTO preguntas (materia_id, texto, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta, dificultad, explicacion) VALUES
(1, '¿Cuál es la derivada de f(x) = 2x³ + 5x - 3?', '6x² + 5', '6x² - 5', '2x² + 5', 'x² + 5', 'a', 'medio', 'La derivada de 2x³ es 6x², y la de 5x es 5'),
(1, '¿Cuál es el límite cuando x tiende a 2 de (x² - 4)/(x - 2)?', '0', '2', '4', '8', 'c', 'medio', 'Factorizar: (x-2)(x+2)/(x-2) = x+2 = 4'),
(1, '¿Cuál es la integral de ∫(3x² + 2x)dx?', 'x³ + x² + C', 'x³ + x + C', '3x³ + 2x + C', '6x + 2 + C', 'a', 'medio', 'La integral de 3x² es x³, la de 2x es x²'),
(1, '¿En qué punto se encuentra el máximo local de f(x) = x² - 4x + 3?', 'x = 0', 'x = 2', 'x = 1', 'x = 3', 'b', 'dificil', 'f\'(x) = 2x - 4 = 0, entonces x = 2'),
(1, '¿Cuál es la continuidad de f(x) = 1/x en x = 0?', 'Continua', 'Discontinua de salto', 'Discontinua infinita', 'Continua por partes', 'c', 'dificil', 'En x=0 hay una discontinuidad infinita'),
(1, '¿Cuál es la serie de Taylor de sin(x) alrededor de x = 0?', 'x - x³/3! + x⁵/5! - ...', 'x + x³/3! + x⁵/5! + ...', '1 - x²/2! + x⁴/4! - ...', 'x²/2! + x⁴/4! + ...', 'a', 'dificil', 'Alternancia de signos y factoriales impares'),
(1, '¿Cuál es la derivada de f(x) = e^x?', 'e^x', 'x·e^x', '1', 'e^(x-1)', 'a', 'facil', 'La derivada de e^x es e^x'),
(1, '¿Cuál es el área bajo la curva y = x² de 0 a 2?', '8/3', '4', '16', '2', 'a', 'medio', '∫(0 a 2) x² dx = [x³/3] = 8/3'),
(1, '¿Cuál es el límite de sin(x)/x cuando x → 0?', '0', '1', '∞', '-1', 'b', 'medio', 'Este es un límite notable igual a 1'),
(1, '¿Cuál es la second derivada de f(x) = 3x⁴ - 2x²?', '36x² - 4', '12x³ - 4x', '36x² + 4', '12x³ + 4x', 'a', 'medio', 'f\'(x) = 12x³ - 4x, f\'\'(x) = 36x² - 4');

-- Programación I - Carrera 1 (Ingeniería)
INSERT INTO preguntas (materia_id, texto, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta, dificultad, explicacion) VALUES
(2, '¿Cuál es el tipo de dato para un número entero en Python?', 'str', 'int', 'float', 'bool', 'b', 'facil', 'int representa números enteros'),
(2, '¿Qué resultado da print(5 // 2)?', '2.5', '2', '3', '2.0', 'b', 'facil', '// es división entera'),
(2, '¿Cuál es la forma correcta de definir una función en Python?', 'function miFuncion():', 'def miFuncion():', 'func miFuncion():', 'function: miFuncion', 'b', 'facil', 'def es la palabra clave para funciones'),
(2, '¿Qué es un bucle for?', 'Una estructura condicional', 'Una forma de repetir código', 'Una función', 'Una librería', 'b', 'facil', 'for permite iterar m
[... contenido truncado ...]
```

------------------------------------------------------------

### TEXT (3 archivos)

#### `requirements.txt`
- **Líneas:** 10
- **Tamaño:** 200 bytes

**Contenido:**
```txt
lask==2.3.0
Flask-SQLAlchemy==3.0.5
Flask-Migrate==4.0.4
Flask-JWT-Extended==4.4.4
Flask-CORS==4.0.0
python-dotenv==1.0.0
PyMySQL==1.1.0
cryptography==41.0.0
Werkzeug==2.3.0
SQLAlchemy==2.0.0
```

------------------------------------------------------------

#### `rutas.txt`
- **Líneas:** 65
- **Tamaño:** 1767 bytes

**Contenido:**
```txt
URL: /
Endpoint: index
Métodos: GET
--------------------------------------------------
URL: /api/carreras
Endpoint: get_carreras
Métodos: GET
--------------------------------------------------
URL: /api/health
Endpoint: health
Métodos: GET
--------------------------------------------------
URL: /api/login
Endpoint: api_login
Métodos: POST
--------------------------------------------------
URL: /api/materias
Endpoint: get_materias
Métodos: GET
--------------------------------------------------
URL: /api/materias/carrera/<int:carrera_id>
Endpoint: get_materias_por_carrera
Métodos: GET
--------------------------------------------------
URL: /api/quiz/preguntas/<int:materia_id>
Endpoint: get_preguntas
Métodos: GET
--------------------------------------------------
URL: /api/rankings/global/racha
Endpoint: rankings_racha
Métodos: GET
--------------------------------------------------
URL: /api/register
Endpoint: api_register
Métodos: POST
--------------------------------------------------
URL: /concursos
Endpoint: concursos
Métodos: GET
--------------------------------------------------
URL: /dashboard
Endpoint: dashboard
Métodos: GET
--------------------------------------------------
URL: /login
Endpoint: login
Métodos: GET
--------------------------------------------------
URL: /quiz
Endpoint: quiz
Métodos: GET
--------------------------------------------------
URL: /rankings
Endpoint: rankings
Métodos: GET
--------------------------------------------------
URL: /registro
Endpoint: registro
Métodos: GET
--------------------------------------------------
URL: /static/<path:filename>
Endpoint: static
Métodos: GET
--------------------------------------------------

```

------------------------------------------------------------

#### `rutas_y_redirecciones.txt`
- **Líneas:** 85
- **Tamaño:** 2859 bytes

**Contenido:**
```txt
======================================================================
RUTAS DE LA APLICACIÓN FLASK
======================================================================

URL: /static/<path:filename>
Endpoint: static
Métodos: GET
----------------------------------------------------------------------
URL: /
Endpoint: index
Métodos: GET
----------------------------------------------------------------------
URL: /login
Endpoint: login
Métodos: GET
----------------------------------------------------------------------
URL: /registro
Endpoint: registro
Métodos: GET
----------------------------------------------------------------------
URL: /quiz
Endpoint: quiz
Métodos: GET
----------------------------------------------------------------------
URL: /rankings
Endpoint: rankings
Métodos: GET
----------------------------------------------------------------------
URL: /concursos
Endpoint: concursos
Métodos: GET
----------------------------------------------------------------------
URL: /dashboard
Endpoint: dashboard
Métodos: GET
----------------------------------------------------------------------
URL: /api/login
Endpoint: api_login
Métodos: POST
----------------------------------------------------------------------
URL: /api/register
Endpoint: api_register
Métodos: POST
----------------------------------------------------------------------
URL: /api/carreras
Endpoint: get_carreras
Métodos: GET
----------------------------------------------------------------------
URL: /api/materias
Endpoint: get_materias
Métodos: GET
----------------------------------------------------------------------
URL: /api/materias/carrera/<int:carrera_id>
Endpoint: get_materias_por_carrera
Métodos: GET
----------------------------------------------------------------------
URL: /api/quiz/preguntas/<int:materia_id>
Endpoint: get_preguntas
Métodos: GET
----------------------------------------------------------------------
URL: /api/rankings/global/racha
Endpoint: rankings_racha
Métodos: GET
----------------------------------------------------------------------
URL: /api/health
Endpoint: health
Métodos: GET
----------------------------------------------------------------------


======================================================================
REDIRECCIONES EN EL CÓDIGO
======================================================================

Archivo: .\export_routes.py
Línea: 24
Destino: /ruta
Código: r'redirect\([\'"]([^\'"]+)[\'"]\)',  # redirect('/ruta')
----------------------------------------------------------------------
Archivo: .\export_routes.py
Línea: 25
Destino: endpoint
Código: r'redirect\(url_for\([\'"]([^\'"]+)[\'"]\)',  # redirect(url_for('endpoint'))
----------------------------------------------------------------------

```

------------------------------------------------------------

## 🤖 GUÍA PARA LA IA
------------------------------------------------------------

### Cómo usar esta documentación:

1. **Estructura del Proyecto**: Consulta la sección de estructura para entender la organización de archivos
2. **Análisis de Código**: Revisa cada archivo para comprender la funcionalidad
3. **Dependencias**: Observa los imports para entender las relaciones entre módulos
4. **Documentación**: Lee los docstrings para comprender el propósito de funciones y clases

### Información de Contexto Importante:

- Este proyecto fue escaneado automáticamente
- El contenido de archivos muy largos puede estar truncado
- Archivos binarios y algunos encodings especiales pueden no mostrarse correctamente
- Los directorios ignorados incluyen: __pycache__, .git, venv, node_modules, etc.

### Recomendaciones al trabajar con este proyecto:

1. Primero lee el archivo README.md si existe
2. Identifica el punto de entrada principal (main.py, app.py, index.html, etc.)
3. Revisa la estructura de carpetas para entender la arquitectura
4. Analiza las dependencias y librerías utilizadas
5. Lee la documentación inline (docstrings, comentarios) para contexto adicional

### Para actualizar esta documentación:

Ejecuta nuevamente el script cuando hagas cambios significativos al proyecto:
```bash
python generar_documentacion.py
```
