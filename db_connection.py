import os 
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
def add_students():
    try:
        connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
        )
        cursor = connection.cursor()
    except mysql.connector.Error:
        print("Unable to connect to the database")
        return
    
    full_name = input("Enter student name: ").strip()
    while not full_name:
        print("Name can't be empty!")
        full_name = input("Enter student name: ").strip()
    while True:
        try:
            age = int(input("Enter student age: "))
            if age <= 0:
                print("Age must be a positive integer!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for age.")
    course = input("enter course name : ").strip()
    while not course:
        print("Course can't be empty!")
        course = input("enter course name : ").strip()
    while True:
        try:
            marks = float(input("Enter student marks: "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for marks.")
        
        

    query = """
    INSERT INTO Students (full_name, age, course, marks)
    VALUES (%s, %s, %s, %s)
    """

    values = (full_name, age, course, marks)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Student added successfully!")
    except mysql.connector.Error:
        print("Database error: Unable to add student.")
    finally:
        cursor.close()
        connection.close()
    
if __name__ == "__main__":
    add_students()