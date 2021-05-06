from datetime import datetime
from typing import List

from .models import Transaction


def create_transactions(raw_transactions: List[List]):
    transactions = [
        Transaction(
            date=datetime.strptime(raw_transaction[0], '%Y-%m-%d'),
            account=int(raw_transaction[1]),
            amount=float(raw_transaction[2]),
        )
        for raw_transaction in raw_transactions
    ]
    Transaction.objects.bulk_create(transactions)
