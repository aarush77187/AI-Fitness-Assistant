import streamlit as st
from FitnessAssistant import FitnessAssistant
from storage import save_data, view_history
import csv

st.title("AI Fitness Assistant")

menu = st.sidebar.selectbox("Menu", ["Add Person", "View History"])

if menu == "Add Person":
    st.header("Enter Your Details")

    name = st.text_input("Name")
    gender = st.selectbox("Gender", ["male", "female"])
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0)
    weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0)
    activity = st.selectbox("Activity Level", [
        "sedentary", "lightly active", "moderately active", "very active"
    ])

    if st.button("Generate"):
        if name.strip() == "":
            st.error("Please enter a name.")
        else:
            try:
                person = FitnessAssistant(name, gender, int(age), height, weight, activity)
                save_data(person)

                st.success(f"Results for {person.name}")
                col1, col2, col3 = st.columns(3)
                col1.metric("BMI", person.bmi)
                col2.metric("Status", person.status())
                col3.metric("Goal", person.goal())

                col4, col5, col6 = st.columns(3)
                col4.metric("BMR", person.bmr())
                col5.metric("Maintenance Cal", person.daily_calories())
                col6.metric("Target Cal", person.target_calories())

                st.metric("Protein", f"{person.protein_requirement()} g/day")
                st.info(f"Diet: {person.diet_plan()}")

                st.subheader("Workout Plan")
                for item in person.workout_plan():
                    st.write("•", item)

            except ValueError as e:
                st.error(str(e))

elif menu == "View History":
    st.header("Fitness History")
    try:
        with open("fitness_history.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) <= 1:
                st.info("No history yet.")
            else:
                headers = rows[0]
                data = rows[1:]
                st.dataframe(
                    [dict(zip(headers, row)) for row in data]
                )
    except FileNotFoundError:
        st.info("No history yet.")