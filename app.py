import streamlit as st
from utils import calculate_bmi, bmi_category, safety_rules
from agents import workout_agent, diet_agent, explanation_agent
from style import apply_style
from progress import save_progress

# --- Page config and styling ---
st.set_page_config("AI Fitness Planner", layout="wide")
apply_style()

st.title("AI-Powered Personalized Workout & Diet Planner")

# --- User input ---
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 15, 60)
    height = st.number_input("Height (cm)", 140, 210)
    weight = st.number_input("Weight (kg)", 35, 150)
    gender = st.selectbox("Gender", ["Male", "Female"])
    disease = st.selectbox("Medical Condition", ["None", "Asthma", "Diabetes", "Knee Pain", "Heart Issues"])

with col2:
    goal = st.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Stay Fit"])
    diet = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian"])
    budget = st.selectbox("Budget", ["Low", "Medium"])
    location = st.selectbox("Workout Location", ["Home", "Gym"])

# --- Generate plan button ---
if st.button("Generate My AI Plan"):
    # 1. Calculate and save health data
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    save_progress(weight, bmi)

    st.subheader("Health Summary")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Category:** {category}")
    st.write(f"**Safety Note:** {safety_rules(disease)}")

    # 2. Define the 'data' dictionary inside the button block
    data = {
        "age": age,
        "bmi": bmi,
        "bmi_category": category,
        "disease": disease,
        "goal": goal,
        "diet": diet,
        "budget": budget,
        "location": location
    }

    # 3. Generate daily plans
    with st.spinner("Generating your personalized weekly plan..."):
        try:
            # Call agents once to get the full week (prevents 429 errors)
            full_workout = workout_agent(data)
            full_diet = diet_agent(data)
            explanation = explanation_agent(data)

            # 4. Display results
            st.success("Plan Generated Successfully!")
            
            st.subheader("Weekly Workout Schedule")
            st.markdown(full_workout)

            st.divider()

            st.subheader("Weekly Diet Schedule")
            st.markdown(full_diet)

            st.divider()

            st.subheader("Plan Explanation & Tips")
            st.markdown(explanation)

        except Exception as e:
            st.error(f"Error communicating with AI: {e}")
            st.info("Try refreshing the page or checking your API key quota.")