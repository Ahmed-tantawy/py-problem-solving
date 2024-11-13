#Dicitionry is the smae like hash table
import time
name = "Tantawy"
age = 22
money = 450.5
happy = True

#list [] = mutubale, most flexible
#Tuple () = Immutable, faster
#set {} - mutuble(add/remove) , unordered(meaning you can't work with indecies), NO duplicates, best for membership testing

fruits = ["apple", "banana", "coconut", "grape"]
for fruit in fruits:
    print(fruit, end=" ")

persons= [{"name":"Tantawy","age":22, "money":450.5, "happy":True},
         {"name":"Tantawy","age":34, "money":450.5, "happy":False},
         {"name":"Tantawy","age":34, "money":450.5, "happy":True}]

for index in range(0, len(persons)):
    time.sleep(2)
    print(persons[index]['age'])