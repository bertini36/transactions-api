from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .actions import (
    get_annual_balances,
    get_monthly_balances,
)


@api_view(['GET'])
def get_annual_balances_view(
    request: Request, account: int = None, year: int = None
) -> Response:
    balance = get_annual_balances(account, year)
    return Response(balance)


@api_view(['GET'])
def get_monthly_balances_view(
    request: Request, account: int = None, year: int = None, month: int = None
) -> Response:
    balances = get_monthly_balances(account, year, month)
    return Response(balances)
