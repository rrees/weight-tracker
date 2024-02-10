import os

import psycopg

from psycopg.rows import dict_row

from . import sql


def _db_url():
    return os.environ["DATABASE_URL"]


def today(weight_in_grams):
    with psycopg.connect(_db_url()) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql.insert_today, {"weight_in_grams": weight_in_grams})


def history():
    with psycopg.connect(_db_url()) as conn:
        with conn.cursor() as cursor:
            results = cursor.execute(sql.history)
            return [r for r in results]


def recent_history():
    with psycopg.connect(_db_url(), row_factory=dict_row) as conn:
        with conn.cursor() as cursor:
            results = cursor.execute(sql.recent_history)
            return [r for r in results]
