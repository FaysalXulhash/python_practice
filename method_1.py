class Student:
    roll = ""
    dept = ""

    def __init__(self, roll, dept):
        self.roll = roll
        self.dept = dept

    def display(self):
        print(f"Roll: {self.roll} \nDepartment: {self.dept}\n\n\n")


a = Student("ASH1825015M", "IIT")
a.display()

b = Student(12, "SE")
b.display()

