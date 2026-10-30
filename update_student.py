import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def update_students():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
)
    cursor = connection.cursor()

    student_id = input("Enter student ID to update: ")

    query = "Select * from students where id = %s"

    cursor.execute (query,(student_id,))
    student = cursor.fetchone()

    if student is None:
        print("Student not found")
    else:
        print("---Student found---")
        print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Course: {student[3]} | Marks: {student[4]} | Created At: {student[5]}")
        print("===== UPDATE STUDENT =====")
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Course")
        print("4. Update Marks")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_name = input("Enter new name: ").strip()
            if not new_name:
                print("Name cannot be empty!")
            else:
                update_query = "update students set full_name =%s where id =%s"
                cursor.execute(update_query,(new_name,student_id))
                connection.commit()
                print("Student name updated successfully!")
        elif choice == "2":
            try:
                new_age = int(input("Enter new age: "))
                if new_age <= 0:
                    print("Age must be a positive integer!")
                else:
                    update_query = "update students set age =%s where id =%s"
                    cursor.execute(update_query,(new_age,student_id))
                    connection.commit()
                    print("Student age updated successfully!")
            except ValueError:
                print("Invalid input! Please enter a valid integer for age.")
        elif choice == "3":
            new_course = input("Enter new course: ").strip()
            if not new_course:
                print("Course cannot be empty!")
            else:
                update_query = "update students set course =%s where id =%s"
                cursor.execute(update_query,(new_course,student_id))
                connection.commit()
                print("Student course updated successfully!")
        elif choice == "4":
            try:
                new_marks = float(input("Enter new marks: "))
                if new_marks < 0 or new_marks > 100:
                    print("Marks must be between 0 and 100!")
                else:
                    update_query = "update students set marks =%s where id =%s"
                    cursor.execute(update_query,(new_marks,student_id))
                    connection.commit()
                    print("Student marks updated successfully!")
            except ValueError:
                print("Invalid input! Please enter a valid number for marks.")
        elif choice == "5":
            print("Going back to the main menu.")
            
    cursor.close()
    connection.close()
if __name__ == "__main__":
    update_students()