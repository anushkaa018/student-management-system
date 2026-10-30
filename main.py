from db_connection import add_students
from view_students import view_all_students
from search_student import search_students
from update_student import update_students
from delete_student import delete_students


def display_menu():
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
def get_choice():
    choice = input("Enter your choice between 1-6: ")
    return choice 
while True:
    display_menu()
    choice = get_choice()
    if choice == "6":
        print("Exiting Student Management System...")
        break
    #elif choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
    elif choice in ("1", "2", "3", "4", "5"):
        if choice == "1":
            add_students()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_students()
        elif choice == "4":
            update_students()
        elif choice == "5":
            delete_students()
    else:
        print("Invalid choice! Please enter a number between 1 and 6")
