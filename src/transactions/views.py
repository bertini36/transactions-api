from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .actions import get_balance, get_balances


@api_view(['GET'])
def get_balances_view(request: Request, year: int = None) -> Response:
    balances = get_balances(year)
    return Response(balances)


@api_view(['GET'])
def get_account_balance_view(
    request: Request, account: int, year: int = None
) -> Response:
    balance = get_balance(account, year)
    return Response(balance)
