# calculator.py

# BMI Calculation
def calculate_bmi(weight, height):

    height_meter = height / 100

    bmi = weight / (height_meter * height_meter)

    return round(bmi, 2)


# BMI Category
def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# BMR Calculation
def calculate_bmr(weight, height, age):

    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    return round(bmr, 2)


# Daily Calories
def daily_calories(bmr):

    calories = bmr * 1.55

    return round(calories, 2)


# Goal Logic
def goal_logic(goal, calories):

    if goal == "Muscle Gain":
        return calories + 400

    elif goal == "Fat Loss":
        return calories - 300

    else:
        return calories