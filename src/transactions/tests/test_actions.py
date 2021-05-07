from datetime import date

from django.test import TestCase

from ..actions import (
    create_transactions,
    get_annual_balance,
    get_annual_balances,
    get_monthly_balances,
)
from ..models import Transaction


class CreateTransactionsActionTest(TestCase):
    def test_create_one_transaction(self):
        raw_transactions = [['2020-01-24', '57300001', '164995.27']]

        transactions = create_transactions(raw_transactions)

        self.assertEqual(len(transactions), 1)

    def test_create_multiple_transactions(self):
        raw_transactions = [
            ['2020-01-24', '57300001', '164995.27'],
            ['2020-11-02', '26000001', '61404.51'],
        ]

        transactions = create_transactions(raw_transactions)

        self.assertEqual(len(transactions), 2)

    def test_create_no_transactions(self):
        raw_transactions = []

        transactions = create_transactions(raw_transactions)

        self.assertEqual(len(transactions), 0)


class GetAnnualBalancesActionTest(TestCase):
    def test_multiple_balances_are_returned_when_multiple_accounts_registered(
        self,
    ):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 1, 1), account=2, amount=20),
            ]
        )

        balances = get_annual_balances(2021)

        self.assertEqual(len(balances), 2)

    def test_no_balances_returned_when_no_transactions_for_a_given_year(self):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 1, 1), account=2, amount=20),
            ]
        )

        balances = get_annual_balances(2020)

        self.assertEqual(len(balances), 0)


class GetAnnualBalanceActionTest(TestCase):
    def test_balance_is_calculated_right_for_one_account_and_specific_year(
        self,
    ):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2020, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
            ]
        )

        balance = get_annual_balance(account=1, year=2021)

        self.assertEqual(balance[0]['balance'], 10)

    def test_an_historic_balance_is_calculated_when_no_year_is_specified(self):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2020, 1, 1), account=1, amount=-10),
            ]
        )

        balance = get_annual_balance(account=1)

        self.assertEqual(balance[0]['balance'], 0)


class GetMonthlyBalances(TestCase):
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


class GetMonthlyBalance(TestCase):
    def test_account_monthly_balances_are_calculated_right(self):
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(2021, 1, 1), account=1, amount=10),
                Transaction(date=date(2021, 2, 1), account=1, amount=-10),
                Transaction(date=date(2021, 1, 1), account=2, amount=20),
                Transaction(date=date(2021, 1, 2), account=2, amount=20),
            ]
        )

        balances = get_monthly_balances()

        self.assertEqual(len(balances), 3)
        self.assertEqual(balances[0]['balance'], 10)
        self.assertEqual(balances[1]['balance'], -10)
        self.assertEqual(balances[2]['balance'], 40)
