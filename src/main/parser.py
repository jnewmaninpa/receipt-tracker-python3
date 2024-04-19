from transaction import Transaction
from html.parser import HTMLParser
import re

class ChaseHTMLParser(HTMLParser):

    def __init__(self):
        self.data_list = []
        super().__init__()

    def handle_data(self, data):
        cleaned = data.strip()
        if len(cleaned) > 0:
            self.data_list.append(cleaned)

    def create_transaction(self):
        account = None
        date = None
        merchant = None
        amount = None
        for i in range(len(self.data_list)):
            current = self.data_list[i]
            if current == "Account":
                account = self.data_list[i + 1]
            elif current == "Date":
                date = self.data_list[i + 1]
            elif current == "Merchant":
                merchant = self.data_list[i + 1]
            elif current == "Amount":
                amount = self.data_list[i + 1]
        return Transaction(merchant, amount, account, date)

def chase_eml_to_transaction(content):
    html_str = content.split("\n\n", 1)[1]
    html_str = re.sub('=\n', '', html_str)
    parser = ChaseHTMLParser()
    parser.feed(html_str)
    return parser.create_transaction()

