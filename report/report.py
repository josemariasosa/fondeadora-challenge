#!/usr/bin/env python3
# coding=utf-8

import os
import configparser

import pandas as pd

from datetime import datetime as dt
from datetime import timedelta
from db import db

config = configparser.ConfigParser()
config.read('config.ini')


class QueryDb:
    """Manage queries to the database."""
    def __init__(self):
        self.conn = db.connect_db()
        self.cursor = self.conn.cursor()

    def get_results(self, query_file: str, params=None) -> pd.DataFrame:
        queries_dir = config['sqlite3']['queries_dir']
        with open(os.path.join(queries_dir, query_file), 'r') as f:
            query = f.read()
            if bool(params):
                query = query.format(**params)

        results = self.cursor.execute(query).fetchall()
        results = pd.DataFrame([dict(r) for r in results])
        return results

    def close(self) -> None:
        self.cursor.close()
        self.conn.close()


def get_period_duration(date_from: str, date_to: str) -> int:
    """Return the seconds between two inclusive dates."""
    _from = dt.strptime(date_from, '%Y-%m-%d')
    _to = (dt.strptime(date_to, '%Y-%m-%d')
           + timedelta(hours=23, minutes=59, seconds=59))

    assert _from < _to, 'Invalid time period!'
    return (_to - _from).seconds


def get_total_reservations(date_from: str, date_to: str) -> pd.DataFrame:
    query_db = QueryDb()
    params = {'date_from': date_from, 'date_to': date_to}
    res1 = query_db.get_results('reserved_vehicles.sql', params)
    res2 = query_db.get_results('rent_duration.sql', params)
    query_db.close()

    if len(res1) > 0 and len(res2) > 0:
        results = pd.merge(res1, res2, how='outer',
                           on=['vehicle_id', 'year', 'model'])

        for column in ['total_rents', 'total_reservations']:
            results[column] = results[column].fillna(0).astype(int)

    elif len(res1) > 0:
        results = res1.copy()
        results['total_rents'] = 0
        results['avg_rent_duration_seconds'] = None

    elif len(res2) > 0:
        results = res2.copy()
        results['total_reservations'] = 0

    else:
        results = pd.DataFrame([])

    return results


def get_vehicle_current_location() -> pd.DataFrame:
    query_db = QueryDb()
    results = query_db.get_results('vehicle_current_location.sql')
    query_db.close()
    return results
