from student import Student
from student_manager import StudentManager


def get_marks():

    marks = {}

    subjects = ["Python","Java", "DBMS","DSA"]

    for subject in subjects:

        while True:

            try:
                mark = float(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return marks

def add_student(manager):

    print("\n===== Add Student =====")


    while True:

        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print("Student ID must be positive.")
                continue

            break

        except ValueError:
            print("Please enter a valid ID.")

    name = input("Enter Name:")

    while not name:
        print("Name cannot be empty.")
        name = input("Enter Name:")

    while True:

        try:
            age = int(input("Enter Age: "))

            if 1 <= age <= 100:
                break

            print("Please enter a valid age.")

        except ValueError:
            print("Please enter a valid number.")

    course = input("Enter Course: ")


    while not course:
        print("Course cannot be empty.")
        course = input("Enter Course:")

    marks = get_marks()

    student = Student(
        student_id,
        name,
        age,
        course,
        marks
    )

    manager.add_student(student)

def search_student(manager):


    print("\n===== Search Student =====")

    try:
        student_id = int(input("Enter Student ID:"))

    except ValueError:
        print("Invalid Student ID.")
        return

    student = manager.search_student(student_id)

    if student:
        student.display_student()

    else:
        print("Student not found.")

def update_student(manager):

    print("\n===== Update Student =====")

    try:
        student_id = int(input("Enter Student ID:"))

    except ValueError:
        print("Invalid Student ID.")
        return

    manager.update_student(student_id)

def delete_student(manager):

    print("\n===== Delete Student =====")

    try:
        student_id = int(input("Enter Student ID: "))

    except ValueError:
        print("Invalid Student ID.")
        return

    manager.delete_student(student_id)


def main():

    manager = StudentManager()

    while True:

        print("\n")
        print("=================================")
        print("    STUDENT MANAGEMENT SYSTEM    ")
        print("=================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("=================================")


        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(manager)

        elif choice == "2":
            manager.view_students()


        elif choice == "3":
            search_student(manager)

        elif choice == "4":
            update_student(manager)

        elif choice == "5":
            delete_student(manager)

        elif choice == "6":
            print("Thank you for choosing Student Management System.")
            break

        else:
            print("Invalid choice. Plase try again.")

if __name__== "__main__":
    main()