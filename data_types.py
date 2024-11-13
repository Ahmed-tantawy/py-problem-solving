grades = [10,59,80]
students = ["student1", "student2", "student3"]

mixed = ["student1", "student2", "student3", 10,59,80 ]
for index in range(len(mixed)):
    print(mixed[index],"\n")
for index in range(len(mixed)):
    print(mixed[index-1])

print(f"the last index of the list  {mixed[-1]} ")