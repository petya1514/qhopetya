import matplotlib.pyplot as plt
plt.switch_backend("TkAgg")


def plot_review_count_by_park(dataset):
    """
    Pie chart: number of reviews per park
    """
    park_counts = {}

    for row in dataset:
        park = row["Branch"]
        park_counts[park] = park_counts.get(park, 0) + 1

    labels = list(park_counts.keys())
    sizes = list(park_counts.values())

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Number of Reviews per Disneyland Park")
    plt.tight_layout()
    plt.show()


def plot_top_locations_for_park(dataset, park_name):
    """
    Bar chart: top 10 locations by average rating for a park
    """
    totals = {}
    counts = {}

    for row in dataset:
        park = row["Branch"].replace("_", " ").lower()
        user_park = park_name.replace("_", " ").lower()

        if park == user_park:
            location = row["Reviewer_Location"]
            try:
                rating = int(row["Rating"])
            except ValueError:
                continue

            totals[location] = totals.get(location, 0) + rating
            counts[location] = counts.get(location, 0) + 1

    averages = {
    loc: totals[loc] / counts[loc]
    for loc in totals
    if counts[loc] >= 5   # minimum review threshold
}

    # Sort and take top 10
    top_10 = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:10]

    locations = [item[0] for item in top_10]
    values = [item[1] for item in top_10]

    plt.figure(figsize=(10, 6))
    plt.bar(locations, values)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating")
    plt.title(f"Top 10 Locations by Average Rating ({park_name})")
    plt.tight_layout()
    plt.show()


def plot_monthly_average_for_park(dataset, park_name):
    """
    Bar chart: average rating per month (Jan–Dec)
    """
    month_totals = {m: 0 for m in range(1, 13)}
    month_counts = {m: 0 for m in range(1, 13)}

    for row in dataset:
        park = row["Branch"].replace("_", " ").lower()
        user_park = park_name.replace("_", " ").lower()

        if park == user_park:
            try:
                rating = int(row["Rating"])
                month = int(row["Year_Month"].split("-")[1])
            except (ValueError, IndexError):
                continue

            month_totals[month] += rating
            month_counts[month] += 1

    months = []
    averages = []

    for m in range(1, 13):
        if month_counts[m] > 0:
            months.append(m)
            averages.append(month_totals[m] / month_counts[m])

    plt.figure(figsize=(10, 6))
    plt.bar(months, averages)
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.title(f"Average Monthly Rating ({park_name})")
    plt.xticks(range(1, 13))
    plt.tight_layout()
    plt.show()
