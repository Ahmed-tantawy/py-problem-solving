def binary_search(arry, search, lowIndex, highIndex):

    while lowIndex <= highIndex:
        mid = lowIndex + (highIndex-lowIndex)//2 #floor 3.6 will be 3
        if arry[mid] == search:
            return mid
        elif arry[mid] < search:
            lowIndex = mid + 1
        else:
            highIndex = mid - 1
    return -1
grades=[10,20,30,40,50,60,70]
grade= sorted(grades)# lenght 7
search =int(input("enter the number that you want to search"))

result = binary_search(grade, search, 0, len(grade)-1)
if result == -1:
    print("not found")
else:
    print("found")