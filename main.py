import csv
import tui
import process
import visual


def load_dataset(filename):
   
    dataset = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dataset.append(row)

    return dataset


def main():
    # -------------------------------------------------
    # SECTION A: Program start & dataset loading
    # -------------------------------------------------

    tui.display_title()

    data = load_dataset("disneyland_reviews.csv")

    tui.display_dataset_loaded(len(data))

    # -------------------------------------------------
    # Main program loop (runs until user exits)
    # -------------------------------------------------

    running = True

    while running:
        choice = tui.display_main_menu()

        # -----------------------------
        # OPTION A: Most Reviewed Parks
        # -----------------------------
        if choice == "A":
            sub_choice = tui.display_menu_a()

            if sub_choice == "1":
                park = tui.get_park_name()
                results = process.get_reviews_for_park(data, park)
                tui.display_reviews(results)

            elif sub_choice == "2":
                park = tui.get_park_name()
                location = tui.get_reviewer_location()
                count = process.count_reviews_by_location(data, park, location)
                tui.display_review_count(count)

            elif sub_choice == "3":
                park = tui.get_park_name()
                year = tui.get_year()
                average = process.average_rating_by_year(data, park, year)
                tui.display_average_rating(average)

            elif sub_choice == "4":
                results = process.average_score_by_park_and_location(data)
                tui.display_location_averages(results)

            else:
                tui.display_invalid_option()

        # --------------------------------
        # OPTION B: Park Ranking & Charts
        # --------------------------------
        elif choice == "B":
            sub_choice = tui.display_menu_b()

            if sub_choice == "1":
                visual.plot_review_count_by_park(data)

            elif sub_choice == "2":
                park = tui.get_park_name()
                visual.plot_top_locations_for_park(data, park)

            elif sub_choice == "3":
                park = tui.get_park_name()
                visual.plot_monthly_average_for_park(data, park)

            else:
                tui.display_invalid_option()

        # --------------------------------
        # OPTION C: Export Data (OOP task)
        # --------------------------------
        elif choice == "C":
             filename = process.export_reviews_per_park(data)
             print(f"Data exported successfully to {filename}")

        # -----------------------------
        # EXIT PROGRAM
        # -----------------------------
        elif choice == "X":
            tui.display_exit_message()
            running = False

        else:
            tui.display_invalid_option()


# -------------------------------------------------
# Program entry point
# -------------------------------------------------
if __name__ == "__main__":
    main()
