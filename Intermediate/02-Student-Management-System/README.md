# Student Management System

## Overview

The **Student Management System** is a console-based Python application developed to manage student records through a menu-driven interface. It allows users to add, view, search, update, delete, and sort student records while generating basic class statistics.

This project was built to strengthen core Python programming concepts such as functions, dictionaries, loops, conditional statements, and CRUD operations.

---

## Features

* Add new student records
* View all students
* Search students by:

  * Roll Number
  * Student Name
* Update student marks
* Delete student records
* Display class statistics:

  * Class average marks
  * Top-performing student
  * Total number of students
* Sort students by:

  * Roll Number
  * Student Name
* Menu-driven interface

---

## Technologies Used

* Python 3
* Functions
* Dictionaries
* Nested Dictionaries
* Loops
* Conditional Statements
* Lambda Functions
* Built-in `sorted()` Function

---

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/Student-Management-System.git
```

### Navigate to the project directory

```bash
cd Student-Management-System
```

### Run the application

```bash
python student_management.py
```

---

## Menu

```text
1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Delete Student
6. Class Statistics
7. Sort Students
8. Exit
```

---

## Sample Data Structure

```python
students = {
    "101": {
        "name": "alice",
        "age": 19,
        "department": "computer science",
        "marks": 92
    }
}
```

---

## Python Concepts Demonstrated

* Modular Programming
* Function Design
* CRUD Operations
* Dictionaries
* Nested Dictionaries
* Iteration
* Searching
* Sorting using `lambda` and `sorted()`
* Menu-Driven Programming
* Data Processing

---

## Future Enhancements

* File handling for permanent data storage
* Input validation using exception handling
* Student grade calculation
* Attendance management
* GPA calculation
* Database integration (SQLite/MySQL)
* Object-Oriented Programming implementation
* Graphical User Interface (GUI)

---

## Author

**Ragul YS**

This project was developed as part of my Python learning journey to strengthen programming fundamentals through the practical implementation of a student record management system.
