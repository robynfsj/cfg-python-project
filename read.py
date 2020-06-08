import csv


# Read the csv file and append each night's sleep as dictionaries in a list.
def read_data():
    data = []
    with open("./data/sleep.csv", "r") as csv_file:
        spreadsheet = csv.DictReader(csv_file, delimiter=";")
        for row in spreadsheet:
            data.append(row)
    return data


# Print data with each dictionary (night's sleep) on a new row.
def view_data():
    data = read_data()
    for row in data:
        print(row)
