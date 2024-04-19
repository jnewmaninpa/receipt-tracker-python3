from transaction import get_transaction_from_csv_line

def save_to_csv(line):
    with open("test.csv", "a") as file:
        file.write(f"{line}\n")

def read_from_csv():
    with open("test.csv", "r") as file:
        lines = file.readlines()
    result = []
    for line in lines:
        result.append(get_transaction_from_csv_line(line))
    return result
