from datetime import date

from django.conf import settings
from django.test import TestCase

from ..actions import create_transactions, get_balances_by_account
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


class GetBalancesByAccountActionTest(TestCase):
    def test_balance_is_calculated_right_for_one_account(self):
        year = settings.DEFAULT_YEAR
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(year, 1, 1), account=1, amount=10),
                Transaction(date=date(year, 1, 1), account=1, amount=-10),
            ]
        )

        balances_by_account = get_balances_by_account(year)

        self.assertEqual(balances_by_account[0]['balance'], 0)

    def test_multiple_balance_are_returned_when_multiple_accounts_registered(
        self,
    ):  # noqa
        year = settings.DEFAULT_YEAR
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(year, 1, 1), account=1, amount=10),
                Transaction(date=date(year, 1, 1), account=2, amount=20),
            ]
        )

        balances_by_account = get_balances_by_account(year)

        self.assertEqual(len(balances_by_account), 2)

    def test_no_balances_returned_when_no_transactions_for_a_given_year(self):
        year = settings.DEFAULT_YEAR
        Transaction.objects.bulk_create(
            [
                Transaction(date=date(year, 1, 1), account=1, amount=10),
                Transaction(date=date(year, 1, 1), account=2, amount=20),
            ]
        )

        balances_by_account = get_balances_by_account(2020)

        self.assertEqual(len(balances_by_account), 0)
