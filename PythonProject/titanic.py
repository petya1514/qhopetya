def display_names(passengers):
    for p in passengers:
        print(p["name"])


def count_survivors(passengers):
    count = 0
    for p in passengers:
        if p["survived"]:
            count += 1
    print("Number of survivors:", count)


def count_by_gender(passengers):
    genders = {}

    for p in passengers:
        gender = p["gender"]
        genders[gender] = genders.get(gender, 0) + 1

    for gender, count in genders.items():
        print(f"{gender}: {count}")


def count_by_age_group(passengers):
    groups = {
        "Child (0-17)": 0,
        "Adult (18-64)": 0,
        "Senior (65+)": 0
    }

    for p in passengers:
        age = p["age"]

        if age <= 17:
            groups["Child (0-17)"] += 1
        elif age <= 64:
            groups["Adult (18-64)"] += 1
        else:
            groups["Senior (65+)"] += 1

    for group, count in groups.items():
        print(f"{group}: {count}")

