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

            # Extraer información específica para archivos Python
            if extension == '.py':
                docstrings = self.extraer_docstrings_python(contenido)
                if docstrings:
                    info_archivo["docstrings"] = docstrings

                # Extraer imports
                imports = [linea.strip() for linea in lineas if linea.strip().startswith(('import ', 'from '))]
                if imports:
                    info_archivo["imports"] = imports[:20]  # Limitar a 20

            return info_archivo

        except Exception as e:
            return {
                "ruta_relativa": str(Path(ruta_archivo).relative_to(self.ruta_raiz)),
                "error": str(e)
            }

    def escanear_proyecto(self):
        """Escanea todo el proyecto y recopila información"""
        print(f"Escaneando proyecto en: {self.ruta_raiz}")

        for root, dirs, files in os.walk(self.ruta_raiz):
            # Filtrar directorios a ignorar
            dirs[:] = [d for d in dirs if not self.debe_ignorar(os.path.join(root, d))]

            for archivo in files:
                ruta_completa = os.path.join(root, archivo)

                if self.debe_ignorar(ruta_completa):
                    continue

                extension = Path(archivo).suffix
                if extension in self.extensiones_codigo or extension == '':
                    info = self.analizar_archivo(ruta_completa)
                    if info:
                        self.archivos_procesados.append(info)
                        print(f"  Procesado: {info.get('ruta_relativa', archivo)}")

    def generar_estructura_arbol(self):
        """Genera una representación en árbol de la estructura del proyecto"""
        estructura = []

        for root, dirs, files in os.walk(self.ruta_raiz):
            if self.debe_ignorar(root):
                continue

            dirs[:] = [d for d in dirs if not self.debe_ignorar(os.path.join(root, d))]

            nivel = root.replace(str(self.ruta_raiz), '').count(os.sep)
            indent = '  ' * nivel
            estructura.append(f"{indent}{os.path.basename(root)}/")

            subindent = '  ' * (nivel + 1)
            for archivo in sorted(files):
                if not self.debe_ignorar(os.path.join(root, archivo)):
                    estructura.append(f"{subindent}{archivo}")

        return '\n'.join(estructura)

    def generar_documentacion(self, archivo_salida="DOCUMENTACION_PROYECTO.md"):
        """Genera el archivo de documentación completo"""
        self.escanear_proyecto()

        doc = []
        doc.append("# Documentación Completa del Proyecto para IA")
        doc.append("=" * 60)
        doc.append(f"\n**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        doc.append(f"**Ruta del proyecto:** {self.ruta_raiz}")
        doc.append("\n")

        # Sección 1: Resumen del Proyecto
        doc.append("## 📊 RESUMEN DEL PROYECTO")
        doc.append("-" * 60)
        doc.append(f"- **Total de archivos procesados:** {self.estadisticas['total_archivos']}")
        doc.append(f"- **Total de líneas de código:** {self.estadisticas['total_lineas']:,}")
        doc.append(f"- **Archivos Python:** {self.estadisticas['archivos_python']}")
        doc.append(f"- **Archivos JavaScript:** {self.estadisticas['archivos_js']}")
        doc.append(f"- **Archivos HTML:** {self.estadisticas['archivos_html']}")
        doc.append(f"- **Archivos CSS:** {self.estadisticas['archivos_css']}")
        doc.append(f"- **Otros archivos:** {self.estadisticas['otros_archivos']}")
        doc.append("\n")

        # Sección 2: Estructura del Proyecto
        doc.append("## 📁 ESTRUCTURA DEL PROYECTO")
        doc.append("-" * 60)
        doc.append("```")
        doc.append(self.generar_estructura_arbol())
        doc.append("```")
        doc.append("\n")

        # Sección 3: Archivos y Contenido Detallado
        doc.append("## 📄 CONTENIDO DETALLADO DE ARCHIVOS")
        doc.append("-" * 60)
        doc.append("\n")

        # Agrupar archivos por tipo
        archivos_por_tipo = {}
        for archivo in self.archivos_procesados:
            tipo = archivo.get('tipo', 'Otro')
            if tipo not in archivos_por_tipo:
                archivos_por_tipo[tipo] = []
            archivos_por_tipo[tipo].append(archivo)

        for tipo, archivos in sorted(archivos_por_tipo.items()):
            doc.append(f"### {tipo.upper()} ({len(archivos)} archivos)")
            doc.append("")

            for archivo in sorted(archivos, key=lambda x: x.get('ruta_relativa', '')):
                doc.append(f"#### `{archivo.get('ruta_relativa', 'Unknown')}`")
                doc.append(f"- **Líneas:** {archivo.get('lineas', 0)}")
                doc.append(f"- **Tamaño:** {archivo.get('tamaño_bytes', 0)} bytes")

                # Mostrar docstrings si existen
                if 'docstrings' in archivo:
                    doc.append("\n**Documentación:**")
                    for nombre, docstring in archivo['docstrings']:
                        doc.append(f"- **{nombre}:**")
                        doc.append(f"  ```")
                        doc.append(f"  {docstring}")
                        doc.append(f"  ```")

                # Mostrar imports si existen
                if 'imports' in archivo:
                    doc.append("\n**Imports:**")
                    for imp in archivo['imports']:
                        doc.append(f"  - `{imp}`")

                # Mostrar contenido
                doc.append("\n**Contenido:**")
                doc.append("```" + archivo.get('extension', '').replace('.', ''))
                doc.append(archivo.get('contenido', '[Sin contenido]'))
                doc.append("```")
                doc.append("\n" + "-" * 60 + "\n")

        # Sección 4: Guía para la IA
        doc.append("## 🤖 GUÍA PARA LA IA")
        doc.append("-" * 60)
        doc.append("""
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
""")

        # Guardar documentación
        ruta_salida = self.ruta_raiz / archivo_salida
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            f.write('\n'.join(doc))

        print(f"\n✅ Documentación generada exitosamente: {ruta_salida}")
        print(f"📊 Total de archivos documentados: {self.estadisticas['total_archivos']}")
        print(f"📝 Total de líneas procesadas: {self.estadisticas['total_lineas']:,}")

        return ruta_salida

def main():
    """Función principal"""
    import sys

    # Obtener ruta del proyecto desde argumentos o usar directorio actual
    ruta_proyecto = sys.argv[1] if len(sys.argv) > 1 else "."

    print("=" * 60)
    print("GENERADOR DE DOCUMENTACIÓN DE PROYECTO PARA IA")
    print("=" * 60)
    print()

    # Crear instancia y generar documentación
    generador = DocumentacionProyecto(ruta_proyecto)
    archivo_generado = generador.generar_documentacion()

    print(f"\n🎉 ¡Listo! Ahora puedes compartir '{archivo_generado.name}' con tu IA.")
    print("\nEste archivo contiene:")
    print("  ✓ Estructura completa del proyecto")
    print("  ✓ Contenido de todos los archivos de código")
    print("  ✓ Estadísticas del proyecto")
    print("  ✓ Documentación extraída (docstrings)")
    print("  ✓ Dependencias e imports")
    print()

if __name__ == "__main__":
    main()