# STUDENT MANAGEMENT SYSTEM

## About the Project

The Student Management System is a simple application built using Python and MySQL to manage student records. It allows users to add, view, search, update, and delete student information through a menu-driven interface.

## Features

- **Add Student:** Add a new student's details to the database.
- **View All Students:** Display all student records.
- **Search Student:** Find a student using their ID.
- **Update Student:** Modify an existing student's information.
- **Delete Student:** Delete a student record after confirmation.
- **Input Validation:** Prevent invalid entries, such as empty names, non-positive ages, and marks outside the 0–100 range.
- **MySQL Database:** Store and manage student records.
- **Environment Variables:** Keep database credentials in a local `.env` file rather than directly in the Python code.

## Technologies Used

- **Python:** Application logic and input validation.
- **MySQL:** Database for storing student records.
- **MySQL Connector/Python:** Connects Python to the MySQL database.
- **python-dotenv:** Loads database configuration from the `.env` file.
- **Git and GitHub:** Version control and project hosting.

## Installation and Setup

### Prerequisites

Before running this project, make sure you have installed:

- Python
- MySQL Server
- MySQL Workbench (optional, for managing the database)

### 1. Clone the Repository

Download or clone the project repository to your computer.

### 2. Install Dependencies

Open the terminal in the project folder and run:

```bash
python -m pip install mysql-connector-python python-dotenv
```

### 3. Create the Database

Open MySQL Workbench and execute:

```sql
CREATE DATABASE student_management;
USE student_management;
```

Create the `Students` table using the schema documented in the project.

### 4. Configure Environment Variables

Create a `.env` file in the project folder with the following settings:

```text
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_local_mysql_password
DB_NAME=student_management
```

Replace `your_local_mysql_password` with your own local MySQL password.

**Security:** Never upload your `.env` file or share your database password.

### 5. Run the Application

Open the terminal in the project folder and run:

```bash
python main.py
```

## Database Schema

The application uses a MySQL database named `student_management` and a table named `Students`.

### Students Table

| Column | Data Type | Description |
|---|---|---|
| `id` | `INT` | Primary key; automatically generated for each student |
| `full_name` | `VARCHAR(50)` | Student's full name; required |
| `age` | `INT UNSIGNED` | Student's age |
| `course` | `VARCHAR(150)` | Student's course; required |
| `marks` | `DECIMAL(5,2)` | Student's marks, between 0 and 100 |
| `created_at` | `DATETIME` | Automatically records when the student record is created |

### SQL Table Creation

```sql
CREATE TABLE Students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(50) NOT NULL,
    age INT UNSIGNED,
    course VARCHAR(150) NOT NULL,
    marks DECIMAL(5,2) CHECK (marks >= 0 AND marks <= 100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
## Project Structure

```text
Student Management/
│
├── main.py              # Main menu and application entry point
├── db_connection.py     # Add student and database connection
├── view_students.py     # View all student records
├── search_student.py    # Search for a student
├── update_student.py    # Update student information
├── delete_student.py    # Delete a student record
├── .env                 # Local database credentials (not uploaded)
├── .gitignore           # Files Git should ignore
└── README.md            # Project documentation
```

## Future Improvements

- Improve database connection handling across all operations.
- Add more automated tests.
- Improve error messages and user experience.
