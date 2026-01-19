import csv

records = []
headings = []


def load_data (file_path):
    global headings, records
    print ("Loading data..")
    with open (file_path, "r") as file :
        reader = csv.reader(file)
        headers = next(reader)
        records = list(reader)
print ("Done")

def run():
    file_path = "titanic.csv"
    load_data(file_path)

    num_records = len(records)
    print(f"Succesfully loaded {num_records} records")


