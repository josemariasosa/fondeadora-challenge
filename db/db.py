#!/usr/bin/env python3
# coding=utf-8

import json
import sqlite3
import configparser

from sqlite3 import Error

config = configparser.ConfigParser().read('config.ini')


        

exit()

def connect_db(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error:
       raise Error

    return conn


def init_db():
    db_file = config[sqlite3][db_file]
    conn = connect_db(db_file)

    if conn:
        cursor = conn.cursor()
        with open('./db/schema.sql') as f:
            cursor.executescript(f.read().decode('utf-8'))
        
        sample_dataset = ['vehicle']
        for dataset in sample_dataset:
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

        cursor.close()
        conn.close()


