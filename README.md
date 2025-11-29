# 📚 Sistema de Préstamo de Libros

Sistema de gestión de préstamos de libros desarrollado en Python que permite administrar libros, usuarios y préstamos de manera eficiente.

## 📋 Descripción

Este sistema permite gestionar el préstamo de libros en una biblioteca, con funcionalidades para:
- Administrar el catálogo de libros
- Gestionar usuarios (Docentes y Estudiantes)
- Registrar y controlar préstamos
- Realizar búsquedas de libros y usuarios
- Controlar límites de préstamos según el tipo de usuario

## ✨ Características

### Gestión de Libros
- ✅ Agregar nuevos libros al catálogo
- ✅ Ver lista completa de libros
- ✅ Buscar libros por nombre o código
- ✅ Control de disponibilidad de libros

### Gestión de Usuarios
- ✅ Registrar usuarios (Docentes y Estudiantes)
- ✅ Ver lista de usuarios
- ✅ Buscar usuarios por nombre o identificación
- ✅ Diferentes límites de préstamos según tipo de usuario:
  - **Docentes**: 8 libros máximo
  - **Estudiantes**: 3 libros máximo

### Gestión de Préstamos
- ✅ Registrar nuevos préstamos
- ✅ Devolver libros prestados
- ✅ Ver préstamos activos
- ✅ Ver historial completo de préstamos
- ✅ Período de préstamo: 15 días
- ✅ Control automático de disponibilidad de libros

## 🏗️ Estructura del Proyecto

```
Sistema Prestamo Libros/
│
├── main.py                 # Punto de entrada principal
├── models/                 # Modelos de datos
│   ├── __init__.py
│   ├── biblioteca.py       # Clase principal Biblioteca
│   ├── libro.py            # Modelo Libro
│   ├── usuario.py          # Modelo Usuario (Docente/Estudiante)
│   └── prestamo.py         # Modelo Prestamo
├── services/               # Servicios
│   └── service_csv.py      # Servicio para manejo de archivos CSV
└── data/                   # Archivos de datos
    ├── libros.csv
    ├── reservas.csv
    └── usuarios.csv
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. Clona o descarga el proyecto:
```bash
git clone <url-del-repositorio>
cd "Sistema Prestamo Libros"
```

2. Instala las dependencias:
```bash
pip install pandas
```

## 📖 Uso

### Ejecutar el Sistema

```bash
python main.py
```

### Menú Principal

El sistema presenta un menú interactivo con las siguientes opciones:

#### 📖 **LIBROS**
1. **Ver Lista de libros** 👁️ - Muestra todos los libros registrados
2. **Agregar nuevo libro** ➕ - Registra un nuevo libro en el sistema
3. **Buscar libro** 🔍 - Busca libros por nombre o código

#### 👤 **USUARIOS**
4. **Ver Lista de Usuarios** 👁️ - Muestra todos los usuarios registrados
5. **Agregar nuevo usuario** ➕ - Registra un nuevo usuario (Docente o Estudiante)
6. **Buscar Usuario** 🔍 - Busca usuarios por nombre o identificación

#### 📝 **PRÉSTAMOS**
7. **Prestar Libro** ➕ - Registra un nuevo préstamo
8. **Devolver Libro** ❌ - Registra la devolución de un libro
9. **Ver libros prestados** 📝🔍 - Muestra todos los préstamos activos
10. **Ver registro de todos los préstamos** 📝🔍 - Muestra el historial completo

## 🔧 Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación
- **pandas** - Manejo de archivos CSV
- **datetime** - Gestión de fechas
- **os** - Operaciones del sistema

## 📝 Modelos de Datos

### Libro
- ID único
- Código (formato: LIB{id}-{copia})
- Nombre
- Disponibilidad (True/False)
- Fecha de registro

### Usuario
- ID único
- Nombre
- Identificación
- Fecha de registro
- Tipo: Docente o Estudiante
- Límite de préstamos según tipo

### Prestamo
- ID único
- ID del libro
- ID del usuario
- Fecha de préstamo
- Fecha estimada de devolución (15 días)
- Fecha de devolución (si ya fue devuelto)

## 🎯 Funcionalidades Técnicas

- **Búsqueda flexible**: Búsqueda por nombre o código/libro, nombre o identificación/usuario
- **Validación de límites**: El sistema previene préstamos que excedan el límite permitido
- **Control de disponibilidad**: Los libros se marcan automáticamente como no disponibles al prestarse
- **Interfaz de consola**: Menú interactivo con limpieza de pantalla para mejor experiencia

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 👨‍💻 Autor

Desarrollado como proyecto de gestión de biblioteca.

## 🔮 Mejoras Futuras

- [ ] Persistencia de datos en base de datos
- [ ] Interfaz gráfica de usuario (GUI)
- [ ] Sistema de notificaciones para préstamos vencidos
- [ ] Reportes y estadísticas
- [ ] Sistema de multas por retrasos
- [ ] Exportación de datos a diferentes formatos

---

**Nota**: Este sistema está diseñado para uso en consola/terminal. Asegúrate de tener Python instalado y las dependencias necesarias antes de ejecutarlo.

