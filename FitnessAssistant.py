class FitnessAssistant:
    def __init__(self, name,gender, age,height, weight,activity):

        if age <= 0:
            raise ValueError("Age must be positive")
        if height<=0:
            raise ValueError("Height must be positive")
        if weight<=0:
            raise ValueError("Weight must be positive")
        
        
        self.name = name
        self.age=age
        self.height_cm = height
        self.height_m = height / 100
        self.weight = weight
        self.gender=gender.lower()
        self.activity=activity.lower()
        if self.activity not in ["sedentary","lightly active","moderately active","very active"]:
            raise ValueError("activity must be any one of sedentary, lightly active, moderately active ,very active" )

        if self.gender not in ["male","female"]:
            raise ValueError("Gender must be male or female")
        self.bmi=self.calculate_bmi()

    def calculate_bmi(self):
        return round(self.weight / (self.height_m ** 2),2)

    def status(self):

        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        

    def goal(self):
        if self.bmi < 18.5:
            return "Muscle Gain"
        elif self.bmi < 25:
            return "Maintain Weight"
        else:
            return "Fat Loss"

    def bmr(self):
        if self.gender =="male":
            bmr=88.362 + (13.397 *self.weight) + (4.799 *self.height_cm) - (5.677 *self.age)
            return round(bmr,2)
        elif self.gender == "female":
            bmr=447.593 + (9.247 *self.weight) + (3.098 *self.height_cm) - (4.330 *self.age)
            return round(bmr,2)
        
    def daily_calories(self):
        if self.activity=="sedentary":

            calories=self.bmr()*1.2
            return round(calories,2)
        
        elif self.activity=="lightly active":
        
            calories=self.bmr()*1.375
            return round(calories,2)
        
        elif self.activity=="moderately active":

            calories=self.bmr()*1.55
            return round(calories,2)
        
        else:
            calories=self.bmr()*1.725
            return round(calories,2)
            
        

    def diet_plan(self):
        goal=self.goal()

        if goal=="Muscle Gain":

            return "High protein diet"
        elif goal=="Fat Loss":

            return "Calorie deficit with high protein"
        
        else:
            return "Balanced diet"
        
    def target_calories(self):

        calories=self.daily_calories()
        goal=self.goal()

        if goal=="Fat Loss":

            return round(calories-500,2)
        
        elif goal=="Muscle Gain":

            return round(calories+300,2)
        
        return round(calories)
    
    def protein_requirement(self):
        goal=self.goal()

        if goal=="Fat Loss":

            return round(self.weight*2)

        elif goal=="Muscle Gain":
            return round(self.weight*1.8)

        else:
            return round(self.weight*1.5)
        
    def workout_plan(self):

        goal=self.goal()

        if self.age < 18:
            return [
                "Pushups",
                "Squats",
                "Planks"
            ]
        
        elif 18 <= self.age <50:

            if goal=="Muscle Gain":

                return ["Day 1: Push",
                        "Day 2: Pull",
                        "Day 3: Legs",
                        "Day 4: Push",
                        "Day 5: Pull",
                        "Day 6: Legs",
                        "Day 7: Rest"
                    ]
            
            elif goal=="Maintain Weight":

                return [
                    "3-4 strength workouts/week",
                    "8k-10k steps daily",
                    "1-2 cardio sessions/week",
                    "Maintain current calories"
                ]
            
            elif goal=="Fat Loss":
               
               return [
                        "HIIT 3 times/week",
                        "10k steps daily",
                        "Any workout split",
                        "Maintain consistency"
                    ]
        else:

            return [
                "Walking",
                "Light Yoga",
                "Stretching"
            ]

    def display(self):
            print("\n-------------------")
            print(f"Name : {self.name}")
            print(f"BMI : {self.bmi}")
            print(f"Status : {self.status()}")
            print(f"Goal : {self.goal()}")
            print(f"BMR : {self.bmr()}")
            print(f"Maintenance Calories : {self.daily_calories()}")
            print(f"Target Calories : {self.target_calories()}")
            print(f"Protein : {self.protein_requirement()} g/day")
            print(f"Diet : {self.diet_plan()}")
            print("Workout Plan:")
            for day in self.workout_plan():
                print("-", day)
            print("-------------------")
