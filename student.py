class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def calculate_percentage(self):
        if not self.marks:
            return 0


        total = sum(self.marks.values())
        number_of_subjects = len(self.marks)

        percentage = total / number_of_subjects
        return percentage

    def calculate_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"
    
        elif percentage >= 60:
            return "C"
    
        elif percentage >= 50:
            return "D"

        else:
            return "F"

    def display_student(self):

        print("\n-----------------------------")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")


        print("Marks :")


        for subject, mark in self.marks.items():
            print(f" {subject}: {mark}")

        print(f"Percentage : {self.calculate_percentage():.2f}%")
        print(f"Grade      : {self.calculate_grade()}")
        print("-------------------------------")

    
