import csv
import os

FILENAME = "fitness_history.csv"
HEADERS = ["Name", "Age", "Gender", "Height", "Weight", "Activity", "BMI", "Status", "Goal", "BMR", "Maintenance Calories", "Target Calories", "Protein (g/day)"]

def save_data(person):
    file_exists = os.path.exists(FILENAME)

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(HEADERS)
        writer.writerow([
            person.name, person.age, person.gender,
            person.height_cm, person.weight, person.activity,
            person.bmi, person.status(), person.goal(),
            person.bmr(), person.daily_calories(),
            person.target_calories(), person.protein_requirement()
        ])

def view_history():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Fitness History ---")
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No history available.")
