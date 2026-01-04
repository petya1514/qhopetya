"""
tui.py
-------
Text User Interface module.
Responsible ONLY for communicating with the user:
- displaying menus
- getting input
- validating input
- showing results passed from other modules

NO data processing must happen here.
"""

def display_title():
    print("=" * 50)
    print("Disneyland Review Analysis Program")
    print("=" * 50)


def display_dataset_loaded(row_count):
    print(f"\nDataset loaded successfully.")
    print(f"Total number of reviews: {row_count}\n")


def display_main_menu():
    print("\nPlease enter one of the following options:")
    print("[A] Most reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Export Data")
    print("[X] Exit")

    choice = input("Your choice: ").strip().upper()
    return choice


# -------------------------------
# MENU A
# -------------------------------
def display_menu_a():
    print("\n[A] View Data Menu")
    print("1. View all reviews for a park")
    print("2. Number of reviews by park and location")
    print("3. Average rating for a park in a given year")
    print("4. Average score per park by reviewer location")

    return input("Select an option: ").strip()


# -------------------------------
# MENU B
# -------------------------------
def display_menu_b():
    print("\n[B] Visualisation Menu")
    print("1. Pie chart of reviews per park")
    print("2. Top 10 locations by average rating for a park")
    print("3. Average monthly rating for a park")

    return input("Select an option: ").strip()


# -------------------------------
# INPUT FUNCTIONS
# -------------------------------
def get_park_name():
    return input("Enter park name: ").strip()


def get_reviewer_location():
    return input("Enter reviewer location: ").strip()


def get_year():
    return input("Enter year (YYYY): ").strip()


# -------------------------------
# OUTPUT FUNCTIONS
# -------------------------------
def display_reviews(reviews):
    if not reviews:
        print("No reviews found.")
    else:
        for review in reviews:
            print(review)


def display_review_count(count):
    print(f"Number of matching reviews: {count}")


def display_average_rating(avg):
    if avg is None:
        print("No data available.")
    else:
        print(f"Average rating: {avg:.2f}")


def display_location_averages(results):
    for park, locations in results.items():
        print(f"\n{park}")
        for location, avg in locations.items():
            print(f"  {location}: {avg:.2f}")


def display_export_message():
    print("\nExporting aggregated data...")


def display_exit_message():
    print("\nExiting program. Goodbye!")


def display_invalid_option():
    print("Invalid option. Please try again.")
