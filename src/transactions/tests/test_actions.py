from django.test import TestCase

from ..actions import create_transactions


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
