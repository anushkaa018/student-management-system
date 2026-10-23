while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print("X--------------------------X")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    user_input = input("Enter your choice (1-6): ")
    if user_input == "1":
        print("you have selected option 1")
    elif user_input == "2":
        print("you have selected option 2")
    elif user_input == "3":
        print("you have selected option 3")
    elif user_input == "4":
        print("you have selected option 4")
    elif user_input == "5":
        print("you have selected option 5")
    elif user_input == "6":
        print("Exiting the program...")
        break
    else:  
        print("Invalid choice. Please try again.")