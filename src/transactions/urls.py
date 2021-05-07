from django.urls import path

from .views import get_balances_view

app_name = 'transactions'

urlpatterns = [
    path(
        r'balances/all/<int:year>/',
        get_balances_view,
        name='get-balances',
    ),
]
