from datetime import datetime
from typing import List

from django.db.models import QuerySet

from .models import Transaction


def create_transactions(raw_transactions: List[List]) -> QuerySet:
    """
    @param raw_transactions: [
        ['yyyy-mm-dd', '123', '200.5'],
        ...
    ]
    """
    transactions = []
    for raw_transaction in raw_transactions:
        (date_str, account_str, amount_str) = raw_transaction
        transactions.append(
            Transaction(
                date=datetime.strptime(date_str, '%Y-%m-%d'),
                account=int(account_str),
                amount=float(amount_str),
            )
        )
    transactions = Transaction.objects.bulk_create(transactions)
    return transactions


def get_annual_balances(year: int = None):
    balances = Transaction.objects.annual_balance(year=year)
    return balances


def get_annual_balance(account: int, year: int = None):
    balance = Transaction.objects.annual_balance(account=account, year=year)
    return balance
