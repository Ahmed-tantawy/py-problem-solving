#what is the oop
#print(type("Hello"))
#hello is an object <class 'str'>
#print(type(int))

# •    Common
# Special
# Methods:
# •    __init__: Initializes
# an
# instance.
# •    __str__: Defines
# a
# string
# representation
# of
# an
# object(used
# by
# print()).
# •    __len__: Allows
# custom
# length
# functionality
# using
# len().
# •    __getitem__: Provides
# custom
# indexing
# behavior.

class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self, name):
        print("I am barking")
    def add_one(self,y):
        return y + 1
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
# d = Dog()
# d.bark()
# print(d.add_one(8))
# print(type(d))
# d = Dog("Tim",14   )
# print(d.set_age(33))
# print(d.name,d.age,d.get_age())
