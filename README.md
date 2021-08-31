# Fondeadora Challenge

Reto para Data Engineer 🏦


## Descripción del reto

Diseñar el modelo de datos para un servicio de renta de vehículos en México. A partir de este modelo implementa un proceso ETL para generar:

- Una tabla agregada con los vehículos más reservados, incluyendo el tiempo promedio de renta. Considera que se requiere tener datos para realizar análisis con diversas dimensiones como año, modelo y otras características del vehículo, ubicación de puntos de salida y retorno, etc.


## Set up inicial

Para el Challenge se utilizó: `Python 3.9.6`.

1. Clonar este repositorio y generar un ambiente virtual:

```sh
python3 -m venv venv
```

2. Ingresar al ambiente virtual e instalar dependencias. Sólo se utiliza `Pandas` para visualizar los reportes en un DataFrame.

```sh
source venv/bin/activate

pip install -r requirements.txt
```

3. Correr el archivo principal.

```sh
python main.py
```


## Descripción del Archivo Principal

Estos son los pasos que se corren:

1. Se crean las tablas en `SQLite3` utilizando el siguiente schema, y se insertan algunos datos de muestra a las mismas:

![](/media/erd.png)

2. Se corre un test para asegurarse de que: 1) todas las tablas fueron creadas y 2) todas las tablas contienen los datos de muestra.

3. Se generan dos reportes, el primero es el que se solicita para el reto (**una tabla agregada con los vehículos más reservados**), y el siguiente regresa la ubicación más actualizada de los vehículos.


## Entregables

- DDL para el modelo de datos transaccional: [**schema.sql**](/db/schema.sql).
- Scripts del ETL (pueden ser stored procedures o scripts en Python u otro lenguaje de programación): [**/report/queries**](/report/queries).
