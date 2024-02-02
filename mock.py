import random
from datetime import datetime, date
from string import ascii_lowercase
import itertools
from typing import List, Tuple, Optional, Union


def iter_alpha_strings() -> str:
    """Generator of strings of form 'a', 'b', ..., 'z', 'aa', 'ab', ..., 'az', 'ba', ..., ..., 'zz', 'aaa', ..."""
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)


def random_dates_between(
        start_date: date,
        end_date: date,
        size: int,
        sort: bool = False
) -> List[date]:
    dt = end_date - start_date

    random_numbers = [random.random() for _ in range(size)]
    if sort:
        random_numbers.sort()

    return [(start_date + dt * f) for f in random_numbers]


def generate_surnames(size: int) -> List[str]:
    return list(itertools.islice(iter_alpha_strings(), size))


def generate_clients(num_clients: int = 100, surnames_unique_fraction: float = .5) -> List[Tuple]:
    cliend_ids = range(1, num_clients + 1)

    num_surnames_unique = int(num_clients * surnames_unique_fraction)
    surnames_unique = generate_surnames(num_surnames_unique)
    surnames = list(itertools.islice(itertools.cycle(surnames_unique), num_clients))

    return list(zip(cliend_ids, surnames))


def generate_orders(
        num_orders: int = 100000,
        num_clients: int = 100,
        min_revenue: float = 100,
        max_revenue: float = 10000,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
) -> List[Tuple]:
    order_ids = range(1, num_orders + 1)

    client_ids = random.choices(range(1, num_clients + 1), k=num_orders)

    drevenue = (max_revenue - min_revenue)
    revenues = [
        random.random() * drevenue + min_revenue
        for _ in range(num_orders)
    ]

    start_date = start_date or date(year=2023, month=6, day=1)
    end_date = end_date or date(year=2026, month=6, day=1)
    datetimes = random_dates_between(start_date, end_date, size=num_orders, sort=True)

    return list(zip(
        order_ids,
        revenues,
        client_ids,
        datetimes,
    ))
