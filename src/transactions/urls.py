from django.urls import path

from .views import get_account_annual_balance_view, get_annual_balances_view

app_name = 'transactions'

urlpatterns = [
    path(
        r'balances/all/<int:year>/',
        get_annual_balances_view,
        name='get-balances',
    ),
    path(
        r'balances/<int:account>/<int:year>/',
        get_account_annual_balance_view,
        name='get-account-balance',
    ),
]
