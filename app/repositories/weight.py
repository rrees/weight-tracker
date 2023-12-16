import os

import psycopg

from . import sql

_db_url = os.environ["DATABASE_URL"]


def today(weight_in_grams):
    with psycopg.connect(_db_url) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql.insert_today, {"weight_in_grams": weight_in_grams})


def history():
    with psycopg.connect(_db_url) as conn:
        with conn.cursor() as cursor:
            results = cursor.execute(sql.history)
            return [r for r in results]
