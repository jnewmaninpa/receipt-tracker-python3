import datetime

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
        self.amount = amount
        self.account = account
        self.transaction_timestamp = transaction_timestamp

        self.notes = notes
        self.receipt = receipt

        if created_timestamp is None:
            self._created_timestamp = datetime.datetime.now()
        else:
            self._created_timestamp = created_timestamp

        if last_update_timestamp is None:
            self._last_update_timestamp = self._created_timestamp
        else:
            self._last_update_timestamp = last_update_timestamp

    def to_csv_line(self):
        line = f"{self.name},{self.amount},{self.account},{self.transaction_timestamp},{self.receipt},{self.notes},{self._created_timestamp},{self._last_update_timestamp}"
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
    parts = csv_line.split(",")
    for i in range(len(parts)):
        if parts[i] == "":
            parts[i] = None
    return Transaction(
            parts[0],
            float(parts[1]),
            parts[2],
            datetime.datetime.fromisoformat(parts[3]),
            receipt=parts[4],
            notes=parts[5],
            created_timestamp=datetime.datetime.fromisoformat(parts[6]),
            last_update_timestamp=datetime.datetime.fromisoformat(parts[7]),
    )
