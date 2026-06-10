# Gestión de Datos de Países en Python

Trabajo Práctico Integrador — Programación 1, UTN Tecnicatura Universitaria en Programación a Distancia.

## Descripción

Sistema de consola desarrollado en Python que permite gestionar información sobre países cargada desde un archivo CSV. Ofrece funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.

## Integrantes

- Leandro Geringer
- Airton Roude

## Requisitos

- Python 3.x

## Instrucciones de uso

1. Clonar el repositorio.
2. Asegurarse de que el archivo `paises.csv` esté en la misma carpeta que `main.py`.
3. Ejecutar el programa con `python main.py`.

## Opciones del menú

1. **Agregar país** — Permite ingresar un nuevo país con nombre, población, superficie y continente.
2. **Actualizar población y superficie** — Modifica los datos de un país existente buscándolo por nombre.
3. **Buscar país por nombre** — Busca países por coincidencia parcial o exacta e muestra sus datos.
4. **Filtrar países** — Filtra por continente, rango de población o rango de superficie.
5. **Ordenar países** — Ordena la lista por nombre, población o superficie (ascendente o descendente).
6. **Mostrar estadísticas** — Muestra país con mayor y menor población, promedios y cantidad por continente.
7. **Guardar y salir** — Guarda los cambios en el CSV y cierra el programa.

## Ejemplos de uso

Agregar un país:

Ingrese el nombre del país que desea agregar: España

Ingrese la población: 47400000

Ingrese la superficie: 505990

Ingrese a que continente pertenece: Europa

País agregado correctamente.

Filtrar países:

Menu:

1- Filtrar por continente.

2- Filtrar por rango de poblacion.

3- Filtrar por rango de superficie.

Ingrese opcion: 1

Ingrese continente: america

Paises de america:

Argentina
Brasil
Canadá



## Estructura del proyecto
├── main.py          # Lógica principal y menú
├── funciones.py     # Funciones de validación
├── paises.csv       # Dataset base
└── README.md

## Repositorio y documentación

- Repositorio: [enlace al repo]
- Documentación PDF: [enlace al PDF]
- Video demostración: [enlace al video]