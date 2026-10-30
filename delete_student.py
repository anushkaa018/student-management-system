import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def delete_students():
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

        student_id = input("Enter student ID to delete: ")
        query = "Select * from students where id = %s"

        cursor.execute (query,(student_id,))
        student = cursor.fetchone()

        if student is None:
            print("Student not found")
        else:
            print("X---Student found---X")
            print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Course: {student[3]} | Marks: {student[4]}")
            
            confirm = input("Are you sure you want to delete this student? (yes/no): ")
            if confirm.lower() == "yes":
                delete_query = "DELETE FROM students WHERE id = %s"
                cursor.execute(delete_query, (student_id,))
                connection.commit()
                print("Student deleted successfully!")
            else:
                print("Deletion canceled.")
    finally:
        try:
            cursor.close()
        finally:
            connection.close()

if __name__ == "__main__":
    delete_students()

