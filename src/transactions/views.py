from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .actions import get_balances


@api_view(['GET'])
def get_balances_view(
    request: Request, year: int = settings.DEFAULT_YEAR
) -> Response:
    balances_by_account = get_balances(year)
    return Response(balances_by_account)
