WORKOUT_PROMPT = """
You are a professional fitness coach. 
Based on these details: Age: {age}, BMI: {bmi}, Condition: {disease}, Goal: {goal}.
Provide a COMPLETE 7-day workout schedule (Monday-Sunday) in one response.
"""

DIET_PROMPT = """
You are an expert nutritionist. 
Based on these details: BMI: {bmi}, Diet: {diet}, Budget: {budget}.
Provide a COMPLETE 7-day diet plan (Monday-Sunday) in one response.
"""

EXPLANATION_PROMPT = """
You are a professional fitness coach and nutritionist AI.
User: Age: {age}, BMI: {bmi}, Disease: {disease}, Goal: {goal}, Diet: {diet}, Budget: {budget}, Location: {location}

Explain in detail why the suggested 7-day workout and diet plan is suitable for the user.
Highlight:
- Why each activity or food is recommended for someone with {disease}.
- Safety and health benefits of this specific routine.
- How to substitute foods or modify workouts safely if they feel pain or fatigue.
"""

