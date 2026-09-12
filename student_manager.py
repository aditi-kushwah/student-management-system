import json
from student import Student


class StudentManager:


    def __init__(self,filename = "students.json"):
        self.filename = filename
        self.students = []

        self.load_students()

    def load_students(self):

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

                for student_data in data:

                    student = Student(
                        student_data["student_id"],
                        student_data["name"],
                        student_data["age"],
                        student_data["course"],
                        student_data["marks"]
                    )

                    self.students.append(student)

        except FileNotFoundError:
            self.students = []

        except json.JSONDecodeError:
            print("Error: JSON file is corrupted.")
            self.students = []
            

    def save_students(self):

        data = []

        for student in self.students:

            student_data = {
                "student_id": student.student_id,
                "name" : student.name,
                "age" : student.age,
                "course" : student.course,
                "marks" : student.marks
            }

            data.append(student_data)

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self, student):

        for existing_student in self.students:

    
            if existing_student.student_id == student.student_id:
                print("Student ID already exists.")
                return

        self.students.append(student)
        self.save_students()

        print("Student added successfully.")

    def view_students(self):

        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display_student()

    def search_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:
                return student

        return None

    def update_student(self, student_id):

        student = self.search_student(student_id)

        if student is None:
            print("Student not found.")
            return

        print("\nLeave field empty if you don't want to change it.")

        new_name = input(f"Enter name [{student.name}]: ")
        new_age = input(f"Enter age [{student.age}]: ")
        new_course = input(f"Enter course [{student.course}]: ")

        if new_name:
            student.name = new_name

        if new_age:
            student.age = int(new_age)

        if new_course:
            student.course = new_course

        self.save_students()

        print("Student updated successfully.")

    def delete_student(self, student_id):

        student = self.search_student(student_id)

        if student is None:
            print("Student not found.")
            return

        self.students.remove(student)

        self.save_students()

    print("Student deleted successfully.")