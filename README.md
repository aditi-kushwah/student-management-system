# Student Management System

A console-based **Student Management System** developed using **Python and Object-Oriented Programming (OOP)**. The application allows users to manage student records, store academic marks, calculate percentages and grades, and persist student data using a JSON file.

## 🚀 Features

* Add new student records
* View all student records
* Search student by Student ID
* Update student information
* Delete student records
* Store marks for:

  * Python
  * Java
  * DBMS
  * DSA
* Calculate student percentage
* Calculate student grade
* Prevent duplicate Student IDs
* Store student data permanently using JSON
* Load existing student data automatically when the application starts
* Input validation and exception handling
* Handle missing or corrupted JSON files

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **JSON**
* **File Handling**
* **Exception Handling**

## 📂 Project Structure

```text
SMS Project/
│
├── main.py
├── student.py
├── student_manager.py
├── students.json
├── README.md
└── .gitignore
```

### File Description

| File                 | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| `main.py`            | Handles the main menu, user input, validation, and application flow |
| `student.py`         | Contains the `Student` class and student-related operations         |
| `student_manager.py` | Manages student records, CRUD operations, and JSON data storage     |
| `students.json`      | Stores student records permanently                                  |
| `README.md`          | Project documentation                                               |
| `.gitignore`         | Specifies files that should not be tracked by Git                   |

## 💡 OOP Concepts Used

This project demonstrates practical use of Object-Oriented Programming concepts.

### Class and Objects

The project uses two main classes:

* `Student`
* `StudentManager`

The `Student` class represents an individual student, while `StudentManager` manages multiple student objects.

### Encapsulation

Student information such as:

* Student ID
* Name
* Age
* Course
* Marks

is stored as attributes inside the `Student` object.

### Methods

The project uses methods to perform operations such as:

* `calculate_percentage()`
* `calculate_grade()`
* `display_student()`
* `add_student()`
* `view_students()`
* `search_student()`
* `update_student()`
* `delete_student()`
* `save_students()`
* `load_students()`

## 📊 Grading System

The application calculates the percentage based on the average marks of all subjects.

|    Percentage | Grade |
| ------------: | :---- |
| 90% and above | A+    |
|     80% – 89% | A     |
|     70% – 79% | B     |
|     60% – 69% | C     |
|     50% – 59% | D     |
|     Below 50% | F     |

## 🔐 Input Validation

The application includes validation for several types of user input.

### Student ID

* Must be a positive integer
* Duplicate Student IDs are not allowed

### Name

* Cannot be empty

### Age

* Must be between 1 and 100

### Course

* Cannot be empty

### Marks

* Must be between 0 and 100
* Invalid numeric input is handled using exception handling

## 💾 Data Storage

Student records are stored in:

```text
students.json
```

The application uses Python's built-in `json` module to save and load student information.

Example student data:

```json
[
    {
        "student_id": 101,
        "name": "Rahul",
        "age": 21,
        "course": "MCA",
        "marks": {
            "Python": 85,
            "Java": 78,
            "DBMS": 90,
            "DSA": 82
        }
    }
]
```

When the application starts, existing records are automatically loaded from the JSON file.

## ⚙️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/aditi-kushwah/student-management-system
```

### 3. Open the Project Folder

```bash
cd "SMS Project"
```

### 4. Run the Application

```bash
python main.py
```

## 🖥️ Application Menu

When the application starts, the following menu is displayed:

```text
=================================
    STUDENT MANAGEMENT SYSTEM
=================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
=================================
Enter your choice:
```

## 📝 Example

When adding a student, the application collects:

```text
Enter Student ID: 101
Enter Name: Rahul
Enter Age: 21
Enter Course: MCA

Enter marks for Python: 85
Enter marks for Java: 78
Enter marks for DBMS: 90
Enter marks for DSA: 82
```

The application then calculates:

```text
Percentage : 83.75%
Grade      : A
```

## 🔄 CRUD Operations

The project implements the basic CRUD operations:

| Operation | Function                               |
| --------- | -------------------------------------- |
| Create    | `add_student()`                        |
| Read      | `view_students()` / `search_student()` |
| Update    | `update_student()`                     |
| Delete    | `delete_student()`                     |

## 🎯 Learning Outcomes

Through this project, I practiced:

* Python programming
* Object-Oriented Programming
* Classes and objects
* Methods and constructors
* CRUD operations
* JSON data handling
* File handling
* Exception handling
* Input validation
* Modular programming
* Git and GitHub

## 🔮 Future Improvements

Possible improvements for future versions:

* Add a graphical user interface using Tkinter
* Add SQLite/MySQL database support
* Add student attendance management
* Add subject-wise performance analysis
* Add authentication/login functionality
* Add CSV/PDF report generation
* Improve input validation during student updates
* Add sorting and filtering of student records

## 👩‍💻 Author

**Aditi Kushwah**

### Project

**Student Management System**

**Technologies:** Python | OOP | JSON | File Handling | Exception Handling | Git & GitHub
# Student Management System

A console-based **Student Management System** developed using **Python and Object-Oriented Programming (OOP)**. The application allows users to manage student records, store academic marks, calculate percentages and grades, and persist student data using a JSON file.

## 🚀 Features

* Add new student records
* View all student records
* Search student by Student ID
* Update student information
* Delete student records
* Store marks for:

  * Python
  * Java
  * DBMS
  * DSA
* Calculate student percentage
* Calculate student grade
* Prevent duplicate Student IDs
* Store student data permanently using JSON
* Load existing student data automatically when the application starts
* Input validation and exception handling
* Handle missing or corrupted JSON files

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **JSON**
* **File Handling**
* **Exception Handling**

## 📂 Project Structure

```text
SMS Project/
│
├── main.py
├── student.py
├── student_manager.py
├── students.json
├── README.md
└── .gitignore
```

### File Description

| File                 | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| `main.py`            | Handles the main menu, user input, validation, and application flow |
| `student.py`         | Contains the `Student` class and student-related operations         |
| `student_manager.py` | Manages student records, CRUD operations, and JSON data storage     |
| `students.json`      | Stores student records permanently                                  |
| `README.md`          | Project documentation                                               |
| `.gitignore`         | Specifies files that should not be tracked by Git                   |

## 💡 OOP Concepts Used

This project demonstrates practical use of Object-Oriented Programming concepts.

### Class and Objects

The project uses two main classes:

* `Student`
* `StudentManager`

The `Student` class represents an individual student, while `StudentManager` manages multiple student objects.

### Encapsulation

Student information such as:

* Student ID
* Name
* Age
* Course
* Marks

is stored as attributes inside the `Student` object.

### Methods

The project uses methods to perform operations such as:

* `calculate_percentage()`
* `calculate_grade()`
* `display_student()`
* `add_student()`
* `view_students()`
* `search_student()`
* `update_student()`
* `delete_student()`
* `save_students()`
* `load_students()`

## 📊 Grading System

The application calculates the percentage based on the average marks of all subjects.

|    Percentage | Grade |
| ------------: | :---- |
| 90% and above | A+    |
|     80% – 89% | A     |
|     70% – 79% | B     |
|     60% – 69% | C     |
|     50% – 59% | D     |
|     Below 50% | F     |

## 🔐 Input Validation

The application includes validation for several types of user input.

### Student ID

* Must be a positive integer
* Duplicate Student IDs are not allowed

### Name

* Cannot be empty

### Age

* Must be between 1 and 100

### Course

* Cannot be empty

### Marks

* Must be between 0 and 100
* Invalid numeric input is handled using exception handling

## 💾 Data Storage

Student records are stored in:

```text
students.json
```

The application uses Python's built-in `json` module to save and load student information.

Example student data:

```json
[
    {
        "student_id": 101,
        "name": "Rahul",
        "age": 21,
        "course": "MCA",
        "marks": {
            "Python": 85,
            "Java": 78,
            "DBMS": 90,
            "DSA": 82
        }
    }
]
```

When the application starts, existing records are automatically loaded from the JSON file.

## ⚙️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the Project Folder

```bash
cd "SMS Project"
```

### 4. Run the Application

```bash
python main.py
```

## 🖥️ Application Menu

When the application starts, the following menu is displayed:

```text
=================================
    STUDENT MANAGEMENT SYSTEM
=================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
=================================
Enter your choice:
```

## 📝 Example

When adding a student, the application collects:

```text
Enter Student ID: 101
Enter Name: Rahul
Enter Age: 21
Enter Course: MCA

Enter marks for Python: 85
Enter marks for Java: 78
Enter marks for DBMS: 90
Enter marks for DSA: 82
```

The application then calculates:

```text
Percentage : 83.75%
Grade      : A
```

## 🔄 CRUD Operations

The project implements the basic CRUD operations:

| Operation | Function                               |
| --------- | -------------------------------------- |
| Create    | `add_student()`                        |
| Read      | `view_students()` / `search_student()` |
| Update    | `update_student()`                     |
| Delete    | `delete_student()`                     |

## 🎯 Learning Outcomes

Through this project, I practiced:

* Python programming
* Object-Oriented Programming
* Classes and objects
* Methods and constructors
* CRUD operations
* JSON data handling
* File handling
* Exception handling
* Input validation
* Modular programming
* Git and GitHub

## 🔮 Future Improvements

Possible improvements for future versions:

* Add a graphical user interface using Tkinter
* Add SQLite/MySQL database support
* Add student attendance management
* Add subject-wise performance analysis
* Add authentication/login functionality
* Add CSV/PDF report generation
* Improve input validation during student updates
* Add sorting and filtering of student records

## 👩‍💻 Author

**Aditi Kushwah**

### Project

**Student Management System**

**Technologies:** Python | OOP | JSON | File Handling | Exception Handling | Git & GitHub
