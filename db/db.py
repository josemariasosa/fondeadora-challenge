#!/usr/bin/env python3
# coding=utf-8

import json
import sqlite3
import configparser

from sqlite3 import Error

config = configparser.ConfigParser()
config.read('config.ini')


def connect_db():
    db_file = config['sqlite3']['db_file']
    conn = sqlite3.connect(db_file)
    return conn


def build_schema(cursor):
    db_schema = config['sqlite3']['db_schema']
    with open(db_schema, 'r') as f:
        cursor.executescript(f.read())
        

def insert_records(cursor):
    sample_data = ['vehicle', 'user', 'location']
    sample_data_dir = config['sqlite3']['sample_data_dir']
    for dataset in sample_data:
        with open(f'./db/sample_data/{dataset}.json', 'r') as ds:
            records = json.load(ds)
        columns = records[0].keys()
        column_text = ', '.join(columns)
        mask = '(' + ', '.join(['?'] * len(columns)) + ')'
        rows = [
            tuple([record[column] for column in columns]) 
            for record in records
        ]
        command = f"INSERT INTO {dataset} ({column_text}) VALUES {mask}"
        cursor.executemany(command, rows)


def init_db():
    conn = connect_db()

    if conn:
        cursor = conn.cursor()

        build_schema(cursor)
        insert_records(cursor)

        conn.commit()

        cursor.close()
        conn.close()
        print('Initialized the database.')


