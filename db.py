import psycopg2
from psycopg2.extras import execute_values
from psycopg2.extensions import connection
from psycopg2 import sql
from typing import List, Tuple

from settings import Settings


def create_database(config: Settings) -> None:
    conn = psycopg2.connect(config.build_postgres_dsn(db_name="postgres"))
    conn.autocommit = True
    cur = conn.cursor()

    check_exists_stmt = sql.SQL(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{config.pg_database}'")
    cur.execute(check_exists_stmt)
    exists = cur.fetchone()
    if not exists:
        create_db_stmt = (
            sql.SQL("CREATE DATABASE {}")
            .format(sql.Identifier(config.pg_database))
        )
        cur.execute(create_db_stmt)

    conn.close()


def create_client_table(conn: connection) -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS client (
                client_id SERIAL PRIMARY KEY,
                surname VARCHAR(100)
            )
            """
        )
    conn.commit()


def create_order_table(conn: connection) -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS "order" (
                order_id SERIAL PRIMARY KEY,
                revenue NUMERIC(12, 2),
                client_id INTEGER REFERENCES client(client_id),
                date DATE
            )
            """
        )
    conn.commit()


def insert_clients(client_list: List[Tuple], conn: connection) -> None:
    with conn.cursor() as cur:
        execute_values(
            cur=cur,
            sql="INSERT INTO client (client_id, surname) VALUES %s",
            argslist=client_list
        )
    conn.commit()


def insert_orders(order_list: List[Tuple], conn: connection) -> None:
    with conn.cursor() as cur:
        execute_values(
            cur=cur,
            sql='INSERT INTO "order" (order_id, revenue, client_id, date) VALUES %s',
            argslist=order_list
        )
    conn.commit()
