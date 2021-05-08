from typing import Iterable

from .models import Transaction
from .utils import delete_key


def get_annual_balances(
    account: int = None, year: int = None
) -> Iterable[dict]:
    balances = Transaction.objects.annual_balance(account=account, year=year)
    return balances


def get_monthly_balances(
    account: int = None, year: int = None, month: int = None
) -> Iterable[dict]:
    balances = Transaction.objects.monthly_balance(
        account=account, year=year, month=month
    )
    balances = delete_key(balances, 'date__month')
    return balances
