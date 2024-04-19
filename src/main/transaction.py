import datetime
import re

class Transaction:
    def __init__(
        self,
        name,
        amount,
        account,
        transaction_timestamp,
        receipt=None,
        notes=None,
        created_timestamp=None,
        last_update_timestamp=None,
        ):
        self.name = name
        self.amount = float(amount.lstrip("$"))
        self.account = account
        
        transaction_timestamp = transaction_timestamp.strip()
        if transaction_timestamp != "":
            try:
                self.transaction_timestamp = datetime.datetime.fromisoformat(transaction_timestamp)
            except ValueError:
                try:
                    self.transaction_timestamp = datetime.datetime.strptime(
                            transaction_timestamp,
                        "%b %d, %Y at %I:%M %p ET"
                    )
                except:
                    raise ValueError(f"cannot parse transaction_timestamp {transaction_timestamp}")
        self.transaction_timestamp = transaction_timestamp

        self.notes = notes
        self.receipt = receipt

        if created_timestamp is None:
            self._created_timestamp = datetime.datetime.now()
        else:
            self._created_timestamp = datetime.datetime.fromisoformat(created_timestamp)

        if last_update_timestamp is None:
            self._last_update_timestamp = self._created_timestamp
        else:
            self._last_update_timestamp = datetime.datetime.fromisoformat(last_update_timestamp)

    def to_csv_line(self):
        line = f"{self.name},{self.amount},{self.account},{self.transaction_timestamp.replace(',', '\\,')},{self.receipt},{self.notes},{self._created_timestamp},{self._last_update_timestamp}"
        # this is okay since name and last_update_timestamp cannot be None
        return line.replace(",None,", ",,")

    def __repr__(self):
        return f"Transaction({self.name}, {self.amount}, {self.account}, {self.transaction_timestamp}, receipt={self.receipt}, notes={self.notes}, created_timestamp={self._created_timestamp}, last_update_timestamp={self._last_update_timestamp})"

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.amount == other.amount and
            self.account == other.account and
            self.transaction_timestamp == other.transaction_timestamp and
            self.receipt == other.receipt and
            self.notes == other.notes and
            self._created_timestamp == other._created_timestamp and
            self._last_update_timestamp == other._last_update_timestamp
        )

def get_transaction_from_csv_line(csv_line):
    csv_line = csv_line.strip().strip("\n")
    parts = re.split(r'(?<!\\),', csv_line)
    if len(parts) < 8:
        return
    for i in range(len(parts)):
        parts[i] = parts[i].replace("\\,", ",")
        if parts[i] == "":
            parts[i] = None
    return Transaction(
            parts[0],
            parts[1],
            parts[2],
            parts[3],
            receipt=parts[4],
            notes=parts[5],
            created_timestamp=parts[6],
            last_update_timestamp=parts[7],
    )
