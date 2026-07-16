import streamlit as st
import pandas as pd
import os

from FitnessAssistant import FitnessAssistant
from storage import save_data

st.set_page_config(
    page_title="AI Fitness Assistant",
    page_icon="🏋️",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title("🏋️ AI Fitness Assistant")
st.caption("BMI • BMR • Calories • Protein • Diet • Workout Planner")

st.sidebar.title("Navigation")
menu = st.sidebar.selectbox(
    "Choose an option",
    ["Add Person", "View History"]
)

# ==========================
# ADD PERSON
# ==========================

if menu == "Add Person":

    st.header("Enter Your Details")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name")
        gender = st.selectbox("Gender", ["male", "female"])
        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            step=1
        )

    with col2:
        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            max_value=250.0
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=10.0,
            max_value=300.0
        )

        activity = st.selectbox(
            "Activity Level",
            [
                "sedentary",
                "lightly active",
                "moderately active",
                "very active"
            ]
        )

    if st.button("Generate Report"):

        if name.strip() == "":
            st.error("Please enter your name.")

        else:

            try:

                person = FitnessAssistant(
                    name,
                    gender,
                    int(age),
                    height,
                    weight,
                    activity
                )

                save_data(person)

                st.success("Report Generated Successfully")

                st.divider()

                c1, c2, c3 = st.columns(3)

                c1.metric("BMI", round(person.bmi, 2))
                c2.metric("Status", person.status())
                c3.metric("Goal", person.goal())

                c4, c5, c6 = st.columns(3)

                c4.metric("BMR", round(person.bmr(), 2))
                c5.metric("Maintenance Calories",
                          round(person.daily_calories(), 2))
                c6.metric("Target Calories",
                          round(person.target_calories(), 2))

                st.metric(
                    "Protein Requirement",
                    f"{person.protein_requirement()} g/day"
                )

                # BMI STATUS

                if person.bmi < 18.5:
                    st.warning("⚠ Underweight")

                elif person.bmi < 25:
                    st.success("✅ Healthy Weight")

                elif person.bmi < 30:
                    st.warning("⚠ Overweight")

                else:
                    st.error("❌ Obese")

                st.progress(min(person.bmi / 40, 1.0))

                with st.expander("🥗 Diet Plan", expanded=True):
                    st.write(person.diet_plan())

                with st.expander("💪 Workout Plan", expanded=True):

                    workout = person.workout_plan()

                    if isinstance(workout, list):
                        for exercise in workout:
                            st.write("•", exercise)
                    else:
                        st.write(workout)

            except ValueError as e:
                st.error(str(e))

# ==========================
# HISTORY
# ==========================

elif menu == "View History":

    st.header("📋 Fitness History")

    if os.path.exists("fitness_history.csv"):

        df = pd.read_csv("fitness_history.csv")

        if df.empty:
            st.info("No history available.")

        else:

            st.dataframe(df, use_container_width=True)

            st.divider()

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Records", len(df))

           # Remove extra spaces from column names
            df.columns = df.columns.str.strip()

            # BMI Chart
            if "BMI" in df.columns:

                st.subheader("📈 BMI History")

                df["BMI"] = pd.to_numeric(df["BMI"], errors="coerce")

                bmi_df = df[["BMI"]].dropna()

                if not bmi_df.empty:
                    st.line_chart(bmi_df)
                else:
                    st.warning("No valid BMI data found.")

            # Weight Chart
            if "Weight" in df.columns:

                st.subheader("⚖️ Weight History")

                df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")

                weight_df = df[["Weight"]].dropna()

                if not weight_df.empty:
                    st.bar_chart(weight_df)
                else:
                    st.warning("No valid Weight data found.")

            st.divider()

            if "Protein (g/day)" in df.columns:

                    st.subheader("🥩 Protein Requirement")

                    df["Protein (g/day)"] = pd.to_numeric(
                        df["Protein (g/day)"],
                        errors="coerce"
                    )

                    protein_df = df[["Protein (g/day)"]].dropna()

                    if not protein_df.empty:
                        st.bar_chart(protein_df)

            with open("fitness_history.csv", "rb") as file:

                st.download_button(
                    label="📥 Download History",
                    data=file,
                    file_name="fitness_history.csv",
                    mime="text/csv"
                )

    else:
        st.info("No history found.")