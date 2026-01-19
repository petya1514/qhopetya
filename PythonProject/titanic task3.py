# Global variable
records = []


def load_data():
    global records
    print("Loading data...", end="")

    # Example data (normally this could come from a file)
    records = [
        {"name": "John Smith", "age": 25},
        {"name": "Anna Brown", "age": 17},
        {"name": "Peter Jones", "age": 40}
    ]

    print("Done!")


def display_passenger_names():
    print("The names of the passengers are...")

    for record in records:
        passenger_name = record["name"]  # local variable
        print(passenger_name)


def run():
    option = input("Enter option: ")

    if option == "1":
        display_passenger_names()
    else:
        print("Error! Option not recognised!")


# Main program
load_data()
run()
