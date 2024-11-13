class Example:
    def instance_method(self):  # Instance method
        return "Instance method called", self

    @classmethod
    def class_method(cls):  # Class method
        return "Class method called", cls

    @staticmethod
    def static_method():  # Static method
        return "Static method called"

e = Example()
print(e.instance_method())
print(Example.class_method())
print(Example.static_method())

#Lambda functions are small, anonymous functions used for short, simple operations.
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8