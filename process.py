def get_reviews_for_park(dataset, park_name):
    """
    Returns all reviews for a given park.
    """
    results = []

    for row in dataset:
        if row["Branch"].strip().lower() == park_name.strip().lower():
            results.append(row)

    return results


def count_reviews_by_location(dataset, park_name, location):
    """
    Returns number of reviews for a park from a specific location.
    """
    count = 0

    for row in dataset:
        if (
            row["Branch"].strip().lower() == park_name.strip().lower()
            and row["Reviewer_Location"].strip().lower() == location.strip().lower()
        ):
            count += 1

    return count


def average_rating_by_year(dataset, park_name, year):
    """
    Returns average rating for a park in a given year.
    """
    total = 0
    count = 0

    for row in dataset:
        if row["Branch"].strip().lower() == park_name.strip().lower():
            if row["Year_Month"].startswith(str(year)):
                try:
                    total += int(row["Rating"])
                    count += 1
                except ValueError:
                    pass

    if count == 0:
        return None

    return total / count


def average_score_by_park_and_location(dataset):
    """
    Returns:
    {
        park: {
            location: average_rating
        }
    }
    """
    temp = {}
    results = {}

    # Step 1: collect totals
    for row in dataset:
        park = row["Branch"]
        location = row["Reviewer_Location"]

        try:
            rating = int(row["Rating"])
        except ValueError:
            continue

        if park not in temp:
            temp[park] = {}

        if location not in temp[park]:
            temp[park][location] = {"total": 0, "count": 0}

        temp[park][location]["total"] += rating
        temp[park][location]["count"] += 1

    # Step 2: calculate averages
    for park in temp:
        results[park] = {}
        for location in temp[park]:
            total = temp[park][location]["total"]
            count = temp[park][location]["count"]
            results[park][location] = total / count

    return results
import csv

def export_reviews_per_park(dataset, filename="export_reviews_per_park.csv"):
    """
    Exports number of reviews per park to a CSV file.
    """
    park_counts = {}

    for row in dataset:
        park = row["Branch"]
        park_counts[park] = park_counts.get(park, 0) + 1

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Park", "Number of Reviews"])

        for park, count in park_counts.items():
            writer.writerow([park, count])

    return filename
