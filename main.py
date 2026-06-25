from FitnessAssistant import FitnessAssistant
from storage import save_data, view_history

while True:
    print("\n===== AI Fitness Assistant =====")
    print("1. Add Person")
    print("2. View History")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":

        name=input("enter name of the person : \n")
        gender=input("enter person's gender : \n")
        try:
            age=int(input("enter person's age : \n"))
            height=float(input("enter height of the person : \n"))
            weight=float(input("enter weight of the person :\n "))

        except ValueError:
            print("Invalid Input!\n")
            continue
        activity=input("enter type of activity( Sedentary / Lightly Active / Moderately Active / Very Active) :  \n")
        try:
            person = FitnessAssistant(
                name,
                gender,
                age,
                height,
                weight,
                activity
            )
            save_data(person)
            person.display()

        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        view_history()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Enter 1, 2, or 3.")


