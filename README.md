## Pipeline de Datos para Gestión de Inventario

Este repositorio contiene un pipeline automatizado desarrollado en Python y SQLite enfocado en la ingesta, limpieza, actualización y auditoría de datos de inventario.

## Arquitectura y Funcionalidades

El proyecto implementa la clase "InventarioBD" para estructurar el flujo de datos (ETL):

1. Ingesta (Load): Creación de la base de datos local y tablas necesarias.
   
2. Transformación (Transform):
   * Corrección de errores de tipografía en nombres de productos.
   * Limpieza de categorías vacías
   
3. Auditoría (Analytics):
   * Filtrado dinámico de ítems disponibles.
   * Cálculo acumulado de métricas de stock.

---

## Tecnologías Utilizadas

* Python 3.x (Programación Orientada a Objetos, módulo os)
* SQLite3 (Manejo de base de datos relacional y sintaxis SQL)

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Elnicardo08/pipeline-inventario-python.git](https://github.com/Elnicardo08/pipeline-inventario-python.git)
