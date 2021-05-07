from django.urls import path

from .views import (
    get_account_annual_balance_view,
    get_annual_balances_view,
    get_account_monthly_balances_view,
    get_monthly_balances_view,
)

app_name = 'transactions'

urlpatterns = [
    path(
        r'annual/balances/all/<int:year>/',
        get_annual_balances_view,
        name='get-annual-balances',
    ),
    path(
        r'annual/balances/<int:account>/<int:year>/',
        get_account_annual_balance_view,
        name='get-account-annual-balance',
    ),
    path(
        r'monthly/balances/all/',
        get_monthly_balances_view,
        name='get-monthly-balances',
    ),
    path(
        r'monthly/balances/<int:account>/',
        get_account_monthly_balances_view,
        name='get-account-monthly-balances',
    ),
    path(
        r'monthly/balances/<int:account>/<int:year>/<int:month>',
        get_account_monthly_balances_view,
        name='get-account-monthly-balance',
    ),
]
