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
- Ver estadísticas globales
- Administrar usuarios

## 🧪 Testing

```bash
# Ejecutar tests
pytest tests/

# Con cobertura
pytest --cov=backend tests/
```

## 📝 Licencia

MIT License - ver [LICENSE](LICENSE)

## 👨‍💻 Autor

Universidad Nacional de la Paz (UNIPAZ)

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📞 Contacto

- Email: soporte@unipaz.edu.co
- Web: https://unipaz.edu.co

## 🎯 Roadmap

### v1.0 (Actual)
- ✅ Sistema de rankings
- ✅ Concursos por eliminación
- ✅ Sistema de logros
- ✅ 3 modos de juego
- ✅ Powerups

### v1.1 (Próximo)
- [ ] Chat en tiempo real
- [ ] Notificaciones push
- [ ] App móvil
- [ ] Certificados PDF
- [ ] Sistema de monedas

### v2.0 (Futuro)
- [ ] Machine Learning (recomendaciones)
- [ ] Modo multijugador
- [ ] Integración con LMS
- [ ] API pública

---

**¡Desarrollado con ❤️ para la educación!**
