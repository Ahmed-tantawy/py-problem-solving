grades = []

# Ask the user for the number of grades
num_grades = int(input("How many grades would you like to enter? "))

# Loop for the specified number of times
for index in range(num_grades):
    grade = input(f"Enter grade {index + 1}: ")
    grades.append(grade)

print("Grades entered:", grades)