from datetime import datetime
from typing import List

from django.db.models import QuerySet

from .models import Transaction
from .utils import delete_key


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


def get_annual_balances(year: int = None) -> List[dict]:
    balances = Transaction.objects.annual_balance(year=year)
    return list(balances)


def get_annual_balance(account: int, year: int = None) -> List[dict]:
    balances = Transaction.objects.annual_balance(account=account, year=year)
    return list(balances)


def get_monthly_balances() -> List[dict]:
    balances = Transaction.objects.monthly_balance()
    balances = delete_key(balances, 'date__month')
    return list(balances)


def get_monthly_balance(
    account: int, year: int = None, month: int = None
) -> List[dict]:
    balances = Transaction.objects.monthly_balance(
        account=account,
        year=year,
        month=month
    )
    balances = delete_key(balances, 'date__month')
    return list(balances)
