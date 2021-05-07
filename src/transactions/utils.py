from csv import reader
from typing import Iterable, List


def get_raw_transactions_from_read_obj(read_obj: Iterable) -> List[List]:
    csv_reader = reader(read_obj)
    next(csv_reader)  # Ignore header
    raw_transactions = list(csv_reader)
    return raw_transactions


def delete_key(dicts: List[dict], key: str):
    return [{k: v for k, v in dict.items() if k != key} for dict in dicts]
