## 🌐 Descripción General

Este proyecto es un sistema de **gestión de biblioteca** desarrollado con **FastAPI** para el backend y **Vue.js** para el frontend. Permite registrar, consultar y gestionar información sobre libros, usuarios y préstamos, ofreciendo una interfaz moderna y una API REST bien estructurada (proyecto final de clases ingeneria software).

## 📊 Tecnologías Utilizadas

### Backend (FastAPI - Python):

- FastAPI
- SQLite
- Pydantic
- Uvicorn

### Frontend (Vue 3 - Vite):

- Vue.js
- Vite
- HTML/CSS/JS

## 📚 Estructura del Proyecto

### Carpeta `app/` (Backend)

- **`models/`**: Define los modelos de datos y esquemas con Pydantic y SQLAlchemy.
- **`repository/`**: Contiene la lógica de acceso a datos (consultas y operaciones con la base de datos).
- **`entrypoints/`**: Contiene los routers de FastAPI para dividir los endpoints por funcionalidad:
  - `libros_router.py`
  - `usuarios_router.py`
- **`db.sqlite3`**: Base de datos SQLite usada para el almacenamiento persistente.
- **`main.py`**: Archivo principal que instancia la aplicación de FastAPI y monta los routers.

### Carpeta `src/` (Frontend)

- Contiene los componentes Vue (como Login, Registro, Listado de Libros, etc).
- Se conecta a la API FastAPI para mostrar y manipular la información.

### Otras Carpetas/Archivos:

- **`public/`**: Archivos estáticos del frontend.
- **`.venv/`**: Entorno virtual de Python.
- **`requirements.txt`**: Dependencias del backend.
- **`vite.config.mjs`**: Configuración de Vite.

## 🔗 Endpoints Disponibles (Resumen)

### Libros

- `GET /api/listar-libros` - Listar todos los libros
- `POST /api/register-libro` - Crear nuevo libro
- `PUT /api/edit-libro` - Editar libro

### Usuarios

- `GET /api/login` - Listar usuarios
- `POST /api/register-user` - Registrar usuario

## ⚖️ Arquitectura del Proyecto

La arquitectura está dividida en **capas**:

- **Modelo**: Define los datos y su estructura (Pydantic / SQLAlchemy).
- **Repositorio**: Acceso a datos y consultas.
- **Rutas**: Puntos de entrada REST organizados por dominio.
- **Frontend**: Se comunica con la API REST para ofrecer una interfaz amigable.

## ✅ Ventajas de esta Arquitectura

- Escalable y mantenible.
- Separación clara de responsabilidades.
- Fácil de testear.
- Posibilidad de reutilizar lógica de negocio sin depender del framework web.

## 🔄 Ejecución del Proyecto

### Backend:

```bash
uvicorn app.main:app --reload
```

### Frontend:

```bash
npm install
npm run dev
```

---
