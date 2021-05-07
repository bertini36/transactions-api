from ..utils import get_raw_transactions_from_read_obj


def test_get_raw_transactions_from_csv_file():
    with open('src/transactions/tests/sample-data10.csv', 'r') as read_obj:
        raw_transactions = get_raw_transactions_from_read_obj(read_obj)

    assert len(raw_transactions) == 9  # File has 10 rows but header is ignored
