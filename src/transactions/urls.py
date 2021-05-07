from django.urls import path

from .views import (
    get_annual_balances_view,
    get_monthly_balances_view,
)

app_name = 'transactions'

urlpatterns = [
    path(
        r'annual/balances/<int:year>/',
        get_annual_balances_view,
        name='get-annual-balances',
    ),
    path(
        r'annual/balances/<int:account>/<int:year>/',
        get_annual_balances_view,
        name='get-account-annual-balance',
    ),
    path(
        r'monthly/balances/',
        get_monthly_balances_view,
        name='get-monthly-balances',
    ),
    path(
        r'monthly/balances/<int:account>/',
        get_monthly_balances_view,
        name='get-account-monthly-balances',
    ),
    path(
        r'monthly/balances/<int:year>/<int:month>/',
        get_monthly_balances_view,
        name='get-specific-month-balances',
    ),
    path(
        r'monthly/balances/<int:account>/<int:year>/<int:month>/',
        get_monthly_balances_view,
        name='get-account-specific-month-balance',
    ),
]
