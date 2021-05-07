from datetime import date

from django.test import TestCase

from ..models import Transaction
from ..queries import get_annual_balances, get_monthly_balances


class GetAnnualBalancesQueryTest(TestCase):
    def test_multiple_balances_are_returned_when_multiple_accounts_registered(
        self,
    ):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 1, 1), account=2, amount=20),
            ]
        )

        balances = get_annual_balances(year=2021)

        self.assertEqual(len(balances), 2)

    def test_no_balances_returned_when_no_transactions_for_a_given_year(self):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 1, 1), account=2, amount=20),
            ]
        )

        balances = get_annual_balances(year=2020)

        self.assertEqual(len(balances), 0)

    def test_balance_is_calculated_right_for_one_account_and_specific_year(
        self,
    ):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2020, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
            ]
        )

        balance = get_annual_balances(account=1, year=2021)

        self.assertEqual(balance[0]['balance'], 10)

    def test_an_historic_balance_is_calculated_when_no_year_is_specified(self):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2020, 1, 1), account=1, amount=-10),
            ]
        )

        balance = get_annual_balances(account=1)

        self.assertEqual(balance[0]['balance'], 0)


class GetMonthlyBalancesQueryTest(TestCase):
    def test_multiple_balances_are_returned_when_multiple_accounts_registered(
        self,
    ):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 1, 1), account=2, amount=20),
            ]
        )

        balances = get_monthly_balances()

        self.assertEqual(len(balances), 2)

    def test_account_monthly_balances_are_calculated_right(self):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 2, 1), account=1, amount=10),
                Transaction(date=date(2021, 1, 1), account=1, amount=20),
                Transaction(date=date(2021, 1, 2), account=1, amount=20),
            ]
        )

        balances = get_monthly_balances(account=1)

        self.assertEqual(len(balances), 2)
        self.assertEqual(balances[0]['balance'], 40)
        self.assertEqual(balances[1]['balance'], 10)

    def test_get_an_specific_account_monthly_balance(self):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 2, 1), account=1, amount=-10),
                Transaction(date=date(2021, 1, 1), account=2, amount=20),
                Transaction(date=date(2021, 1, 2), account=2, amount=20),
            ]
        )

        balances = get_monthly_balances(account=1, year=2021, month=1)

        self.assertEqual(len(balances), 1)
        self.assertEqual(balances[0]['balance'], 10)
