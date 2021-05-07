from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .actions import (
    get_annual_balance,
    get_annual_balances,
    get_monthly_balances,
)


@api_view(['GET'])
def get_annual_balances_view(request: Request, year: int = None) -> Response:
    balances = get_annual_balances(year)
    return Response(balances)


@api_view(['GET'])
def get_account_annual_balance_view(
    request: Request, account: int, year: int = None
) -> Response:
    balance = get_annual_balance(account, year)
    return Response(balance)


@api_view(['GET'])
def get_monthly_balances_view(request: Request) -> Response:
    balances = get_monthly_balances()
    balances = [
        {k: v for k, v in balance.items() if k != 'date__month'}
        for balance in balances
    ]
    return Response(balances)
