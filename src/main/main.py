from transaction import Transaction
from parser import chase_eml_to_transaction

def main():
    print("Welcome to Receipt Tracker\n\n")

    while(True):
        print("0: Exit")
        print("1: Enter new transaction")
        print("2: Created transaction from eml")
        selection = input("Selection: ")
        if selection == "0":
            break
        elif selection == "1":
            print("Please enter the following details")
            name = input("Name: ")
            amount = input("Amount: ")
            account = input("Account: ")
            time_stamp = input("Time: ")
            notes = input("Notes (optional): ")
            receipt = input("Receipt (optional): ")
            transaction = Transaction(name, amount, account, time_stamp, notes=notes, receipt=receipt)
            save_to_csv(transaction.to_csv_line())
        elif selection == "2":
            path = input("File path: ").strip()
            with open(path) as file:
                transaction = chase_eml_to_transaction(file.read())
            save_to_csv(transaction.to_csv_line())
        else:
            print("not a valid selection")

def save_to_csv(line):
    with open("test.csv", "a") as file:
        file.write(f"{line}\n")


if __name__ == "__main__":
    main()
