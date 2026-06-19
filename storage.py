import csv
import os

def save_data(person):

    file_exists = os.path.isfile("fitness_history.csv")

    with open("fitness_history.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Name",
                "BMI",
                "Goal",
                "Target Calories",
                "Protein"
            ])

        writer.writerow([
            person.name,
            person.bmi,
            person.goal(),
            person.target_calories(),
            person.protein_requirement()
        ])
