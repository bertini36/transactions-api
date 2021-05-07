from django.urls import path

from .views import get_balances_by_account_view

app_name = 'transactions'

urlpatterns = [
    path(
        r'balances/by/account/<int:year>/',
        get_balances_by_account_view,
        name='get-balances-by-account',
    ),
]
