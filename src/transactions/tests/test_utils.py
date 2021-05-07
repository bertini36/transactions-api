from ..utils import get_raw_transactions_from_read_obj, delete_key


def test_get_raw_transactions_from_csv_file():
    with open('src/transactions/tests/sample-data10.csv', 'r') as read_obj:
        raw_transactions = get_raw_transactions_from_read_obj(read_obj)

    assert len(raw_transactions) == 9  # File has 10 rows but header is ignored


def test_delete_key_of_a_dict():
    data = [{'a': 1, 'b': 2}]

    data = delete_key(data, 'a')

    assert set(data[0].keys()) == {'b'}


def test_delete_key_of_multiples_dicts():
    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]

    data = delete_key(data, 'a')

    assert len(data) == 2
    assert set(data[0].keys()) == {'b'}
    assert set(data[1].keys()) == {'b'}


def test_no_delete_when_key_is_not_in_dict():
    data = [{'a': 1, 'b': 2}]

    data = delete_key(data, 'c')

    assert set(data[0].keys()) == {'a', 'b'}
