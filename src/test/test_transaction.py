import unittest
import datetime

from main.transaction import *

class TestTransaction(unittest.TestCase):

    def test_repr(self):
        transaction = Transaction(
            "Coffee",
            1.23,
            "Bank 1234",
            None
        )
        self.assertEqual(
            transaction.__repr__(),
            f"Transaction(Coffee, 1.23, Bank 1234, None, receipt=None, notes=None, created_timestamp={transaction._created_timestamp}, last_update_timestamp={transaction._last_update_timestamp})"
        )

    def test_get_transaction_from_csv_line(self):
        transaction = Transaction(
            "Coffee",
            1.23,
            "Bank 1234",
            datetime.datetime(2000,1,1,1,1,1),
            receipt=None,
            notes="These are notes",
            created_timestamp=datetime.datetime.now(),
            last_update_timestamp=datetime.datetime.now(),
 
        )
        result = get_transaction_from_csv_line(f"Coffee,1.23,Bank 1234,2000-01-01 01:01:01,,These are notes,{transaction._created_timestamp},{transaction._last_update_timestamp}")
        self.assertEqual(result, transaction)

    def test_to_csv_line(self):
        transaction = Transaction(
            "Coffee",
            1.23,
            "Bank 1234",
            datetime.datetime(2000,1,1,1,1,1),
            receipt=None,
            notes="These are notes",
            created_timestamp=datetime.datetime.now(),
            last_update_timestamp=datetime.datetime.now(),
 
        )
        result = transaction.to_csv_line()
        expected = f"Coffee,1.23,Bank 1234,2000-01-01 01:01:01,,These are notes,{transaction._created_timestamp},{transaction._last_update_timestamp}"
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()
