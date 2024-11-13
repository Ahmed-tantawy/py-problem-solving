num = int(input("How many num ?")) 
total_sum = 0

# The for loop automatically initializes n to the first value in the range (which is 0).
for n in range (num):
    numbers=float(input("Enter any number "))
    total_sum+=numbers

avg = total_sum/num

print("Average is :", avg)
