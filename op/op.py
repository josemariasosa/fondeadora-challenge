#!/usr/bin/env python3
# coding=utf-8

import os
import json
import sqlite3
import configparser

from db import db

config = configparser.ConfigParser()
config.read('config.ini')


def get_operations() -> list:
    data_dir = config['sqlite3']['sample_data_dir']
    with open(os.path.join(data_dir, 'operations.json'), 'r') as f:
        return json.load(f)


def create_new_registry(operation: dict) -> None:
    conn = connect_db()

    if conn:
        cursor = conn.cursor()
        


    sqlite3.execute(
        'INSERT INTO service ()'

        vehicleId
userId
status
createdAt
type
    )

    conn.close()


def run_operations() -> None:
    operations = get_operations()

    for operation in operations:
        create_new_registry(operation)

    print(operations)
    exit()