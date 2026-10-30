import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def search_students():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = connection.cursor()
    except mysql.connector.Error:
            print("Unable to connect to the database.")
            return
    try:

        student_id = input("Enter student ID: ")
        query = "Select * from students where id = %s"

        cursor.execute (query,(student_id,))
        student = cursor.fetchone()

        if student is None:
            print("Student not found")
        

        else:
            print("---Student found---")
            print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Course: {student[3]} | Marks: {student[4]} | Created At: {student[5]}")
    finally:
        try:
            cursor.close()
        finally:
            connection.close()
    
if __name__ == "__main__":
    search_students()