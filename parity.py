        
from datetime import datetime
start_time = datetime.now()


def main():
    x = int(input("What's x?  "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return  n % 2 == 0 

main()


result = sum(range(1000000))

end_time = datetime.now()

execution_time = end_time - start_time
print(f"Execution time: {execution_time}")
