import sqlite3


def create_table():
    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        height FLOAT,
        weight FLOAT,
        bmi FLOAT,
        calories FLOAT,
        goal TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_user(age, height, weight, bmi, calories, goal):
    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users(age,height,weight,bmi,calories,goal)
    VALUES(?,?,?,?,?,?)
    """, (age, height, weight, bmi, calories, goal))

    conn.commit()
    conn.close()


create_table()