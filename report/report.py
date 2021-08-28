#!/usr/bin/env python3
# coding=utf-8

import os
import sqlite3
import configparser

import pandas as pd

from db import db

config = configparser.ConfigParser()
config.read('config.ini')


def get_total_reservations():
    conn = db.connect_db()
    conn.row_factory = sqlite3.Row

    if conn:
        cursor = conn.cursor()
        procedures = config['report']['procedures']
        with open(procedures, 'r') as f:
            res = cursor.execute(f.read()).fetchall()
            res = pd.DataFrame([dict(r) for r in res])
            print(res)
            print('lol')

        cursor.close()
        conn.close()

