records = []


def load_data():
    global records
    print("Loading data...", end="")


    records = [
        [1, 1, "John.."],
        [2, 0, "Anna.."],
        [3, 1, "Peter.."],
    ]

    print("Done!")
    print(f"Successfully loaded {len(records)} records.\n")

def display_num_survivors():
    num_survivors = 0
    survive_idx = headings.index('Survivor')
    for record in records:
        if record[survive_idx] == '1':
            num_survivors += 1


    if survival_status == 1:
        print("Survivor is alive.")



