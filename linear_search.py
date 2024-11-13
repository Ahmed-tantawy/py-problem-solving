grades = [10, 8, 7, 6, 5, 4, 3, 2, 1]
def linear_search(arry,query):
    for index in range(len(arry)):
        if arry[index] == query:
            return index
    return -1

grades = [10, 8, 7, 6, 5, 4, 3, 2, 1]
search = int(input("Enter the number"))
result = linear_search(grades, search)
if result == -1:
    print("Not found")
else:
    print("Found")

#liner serch
#O(n)

#Binary search
#O(log n)