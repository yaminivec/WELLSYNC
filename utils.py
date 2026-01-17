# utils.py

def calculate_bmi(weight, height):
    """
    Calculates BMI given weight (kg) and height (cm)
    """
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)


def bmi_category(bmi):
    """
    Returns BMI category string
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def safety_rules(disease):
    """
    Returns safety restrictions for given disease
    """
    rules = {
        "Asthma": "Avoid HIIT and sprinting",
        "Diabetes": "Avoid long fasting workouts",
        "Knee Pain": "Avoid jumping and running",
        "Heart Issues": "Avoid high intensity workouts",
        "None": "No restrictions"
    }
    return rules.get(disease, "Consult doctor")
