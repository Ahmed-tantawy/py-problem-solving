class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students) if self.students else 0  # Avoid division by zero

# Create Student instances
s1 = Student("John", 19, 95)
s2 = Student("Tomy", 16, 44)
s3 = Student("Sara", 18, 88)

# Create a Course instance
course = Course("Science", 3)

# Add students to the course
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

# Print the average grade
print("Average grade:", course.get_average_grade())