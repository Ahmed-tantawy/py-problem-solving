# grades = [10, 15, 20]
# print(grades)
# grades[0] =13
# print(grades)

student_grade= [5,10,6,15,20]
not_student_grade=[4,8,2,6,0]
not_student_grade.sort(reverse=True)
#lsit.appent to an elment in the end

#bubble sort algorthim
#1) lenght of the array
# lenght= len(student_grade)
# #2)loop on the elemnets of the array
# for index in range(0, lenght-1):
#     first_grade = student_grade[index]
#     second_grade = student_grade[index+1]
#     if first_grade > second_grade:
#         student_grade[index] = second_grade
#         student_grade[index+1] = first_grade
print(sorted(student_grade))
print(not_student_grade)
