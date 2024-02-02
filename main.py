import psycopg2
from datetime import date

from mock import generate_clients, generate_orders
from settings import Settings
from db import create_database, insert_orders, insert_clients, create_client_table, create_order_table


def main():
    config = Settings()

    num_clients = 50
    num_orders = 20000
    min_revenue = 50
    max_revenue = 5000
    start_date = date(year=2023, month=6, day=1)
    end_date = date(year=2026, month=6, day=1)

    clients = generate_clients(
        num_clients=num_clients,
        surnames_unique_fraction=.3
    )
    orders = generate_orders(
        num_orders=num_orders,
        num_clients=num_clients,
        min_revenue=min_revenue,
        max_revenue=max_revenue,
        start_date=start_date,
        end_date=end_date
    )

    create_database(config=config)

    with psycopg2.connect(config.build_postgres_dsn()) as conn:
        create_client_table(conn)
        create_order_table(conn)

    with psycopg2.connect(config.build_postgres_dsn()) as conn:
        insert_clients(clients, conn)
        insert_orders(orders, conn)


if __name__ == '__main__':
    main()
