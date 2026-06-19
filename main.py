from FitnessAssistant import FitnessAssistant
from storage import save_data
p=[]
try:
    n=int(input("enter number of people : "))
except ValueError:
    print("Enter a valid number")
    exit()

for i in range(n):
    name=input("enter name of the person : ")
    gender=input("enter person's gender : ")
    try:
        age=int(input("enter person's age : "))
        height=float(input("enter height of the person : "))
        weight=float(input("enter weight of the person : "))

    except ValueError:
        print("Invalid Input!")
        continue
    activity=input("enter type of activity( Sedentary / Lightly Active / Moderately Active / Very Active) :  ")
    try:
        person = FitnessAssistant(
            name,
            gender,
            age,
            height,
            weight,
            activity
        )

        p.append(person)
        save_data(person)

    except ValueError as e:
        print(e)
for i in p:
    i.display()

