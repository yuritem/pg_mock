# pg_mock

A simple example of how to populate a PostgreSQL database with mock data using Python.

## Requirements

- [`psycopg2`](https://pypi.org/project/psycopg2/) &mdash; PostgreSQL database adapter
- [`pydantic`](https://docs.pydantic.dev/latest/) &mdash; models & validation (for config/settings)

## Usage

- Install requirements
- Fill the `.env` file in the project root with postgres settings (find example file in `.env.example`)
- Edit `main.main()` to specify amount of data generated and its properties.
- Run `main.py`
