from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .actions import get_balances_by_account


@api_view(['GET'])
def get_balances_by_account_view(request: Request) -> Response:
    balances_by_account = get_balances_by_account()
    return Response(balances_by_account)
