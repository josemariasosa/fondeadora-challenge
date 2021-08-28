#!/usr/bin/env python3
# coding=utf-8

import os
import json
import sqlite3
import configparser

from sqlite3 import Connection, Cursor

config = configparser.ConfigParser()
config.read('config.ini')

SAMPLE_DATASETS = [
    'vehicle', 'customer', 'location', 'reservation', 'rent'
]


def connect_db() -> Connection:
    db_file = config['sqlite3']['db_file']
    conn = sqlite3.connect(db_file)
    return conn


def build_schema(cursor: Cursor) -> None:
    db_schema = config['sqlite3']['db_schema']
    with open(db_schema, 'r') as f:
        cursor.executescript(f.read())
        

def insert_records(cursor: Cursor) -> None:
    data_dir = config['sqlite3']['sample_data_dir']
    for dataset in SAMPLE_DATASETS:
        with open(os.path.join(data_dir, f'{dataset}.json'), 'r') as ds:
            records = json.load(ds)
        if len(records) > 0:
            columns = records[0].keys()
            column_text = ', '.join(columns)
            mask = '(' + ', '.join(['?'] * len(columns)) + ')'
            rows = [
                tuple([record[column] for column in columns]) 
                for record in records
            ]
            command = f"INSERT INTO {dataset} ({column_text}) VALUES {mask};"
            cursor.executemany(command, rows)


def init_db() -> None:
    conn = connect_db()

    if conn:
        cursor = conn.cursor()

        build_schema(cursor)
        insert_records(cursor)

        conn.commit()
        cursor.close()
        conn.close()
        print('Initialized the database.')


def test() -> None:
    conn = connect_db()
    assert bool(conn), 'Connection unavailable!'
    
    cursor = conn.cursor()
    for dataset in SAMPLE_DATASETS:
        result = cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{dataset}';"
        ).fetchall()
        assert len(result) > 0, f'Table {dataset} not found!' 
        
        result = cursor.execute(
            f"SELECT * FROM {dataset};"
        ).fetchall()
        assert len(result) > 0, f'Values not inserted to Table {dataset}'

    conn.close()
    print('All database tests passed.')
