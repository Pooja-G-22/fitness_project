from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import save_user

app = FastAPI()

# CORS connection for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# BMI category
def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    else:
        return "Overweight"


# BMR calculation
def calculate_bmr(weight, height, age):

    # Formula for male/female average
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    return bmr


# Goal based calories
def goal_logic(goal, calories):

    if goal == "Muscle Gain":
        return calories + 500

    elif goal == "Weight Loss":
        return calories - 500

    else:
        return calories


# Diet recommendation
def diet_plan(goal):

    if goal == "Muscle Gain":
        return "High Protein Diet (Eggs, Chicken, Paneer, Milk)"

    elif goal == "Weight Loss":
        return "Low Carb Diet (Salad, Fruits, Oats, Vegetables)"

    else:
        return "Balanced Diet (Rice, Vegetables, Protein)"


# Workout recommendation
def workout_plan(goal):

    if goal == "Muscle Gain":
        return "Pushups, Pullups, Squats, Dumbbells"

    elif goal == "Weight Loss":
        return "Running, Cycling, Cardio, Skipping"

    else:
        return "Walking, Yoga, Stretching"


# Home route
@app.get("/")
def home():

    return {
        "message": "AI Fitness System Running Successfully"
    }


# Main API
@app.post("/profile")
def create_profile(data: dict):

    # User input
    age = data["age"]
    weight = data["weight"]
    height = data["height"]
    goal = data["goal"]

    # BMI
    bmi = weight / ((height / 100) ** 2)
    body_type = bmi_category(bmi)

    # BMR
    bmr = calculate_bmr(weight, height, age)

    # Calories according to goal
    final_calories = goal_logic(goal, bmr)

    # Diet + Workout
    diet = diet_plan(goal)
    workout = workout_plan(goal)

    # Save to SQLite database
    save_user(
        age,
        height,
        weight,
        round(bmi, 2),
        round(final_calories, 2),
        goal
    )

    # API response
    return {

        "BMI": round(bmi, 2),

        "BodyType": body_type,

        "Calories": round(final_calories, 2),

        "Diet": diet,

        "Workout": workout
    }