import psycopg2
from db import db

exit()

conn = psycopg2.connect(
    dbname='fonderent',
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)

vehicles = [
    {
        'year': 2013,
        'make': 'volkswagen',
        'model': 'jetta',
        'motor': '4 cil 2.0 lts'
    },
    {
        'year': 2014,
        'make': 'volkswagen',
        'model': 'jetta',
        'motor': '4 cil 2.0 lts'
    },
    {
        'year': 2015,
        'make': 'volkswagen',
        'model': 'jetta',
        'motor': '4 cil 2.0 lts'
    }
]

with conn.cursor() as cursor:
    cursor.execute('DROP TABLE IF EXISTS vehicles')
    cursor.execute("""
        CREATE TABLE vehicles (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            motor TEXT NOT NULL
        );
    """)
    
    for vehicle in vehicles:
        cursor.execute(
            'INSERT INTO vehicles (year, make, model, motor) values (%s, %s, %s, %s)',
            (vehicle['year'], vehicle['make'], vehicle['model'], vehicle['motor'])
        )

    conn.commit()

conn.close()

