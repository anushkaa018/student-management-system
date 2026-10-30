import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def view_all_students():
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
        cursor.execute("SELECT * FROM Students")
        results = cursor.fetchall()

        if not results:
            print("No students found.")
        else:
            print("===== ALL STUDENTS =====")
            for student in results:
                # print(student[1])
                print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Course: {student[3]} | Marks: {student[4]} | Created At: {student[5]}")
    finally:
        try:
            cursor.close()
        finally:
            connection.close()

if __name__ == "__main__":
    view_all_students()