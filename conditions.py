import time

start_time = time.time()

score = float(input("what's your Score: "))

if score >= 90:
    print("Grade: A ")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



result = sum(range(10000000))

end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
