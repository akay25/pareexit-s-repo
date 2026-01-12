# Day 3: Advanced OOP concepts

# Task 1:
# Nested(Inner) class means a class inside a class

class outer:  # outer class
    class Inner:  # inner class
        pass

# Task 2:
# 1. Instance method:
# -> using self as a parameter for pointing instance of the class
# -> they access and modify instance state through self and class state through self.__class__
# -> common methods in python classes

# 2. Class method:
# -> using cls parameter for pointing to the class itself
# -> they modify class level state through cls, but they can't modify individual instance state

# 3. Static method:
# -> don't take self and cls as a parameters
# -> they can't modify instance or class state directly
# -> mainly use for organizational purposes and namespacing

class demoClass:
    def instance_method(self):
        return ("Instance method called", self)
    
    @classmethod
    def class_method(cls):
        return ("Class method called", cls)

    @staticmethod
    def static_method():
        return ("Static method called",)
    
# Task 3:
# 1. Inheritance:
# -> that allows to inherite instance or methods from another class

class Animal:
    def __init__(self, name):
        self. name
    
    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info()
d.sound()

# 2. Constructors:
# -> generally used for instantiating an object
# -> task to assign values to the data members of the class when an object of the class is created
# -> __init__ method is called the constructor

def __init__(self):
    #body of the constructor
    pass

# super():
# -> allows us to access the temporary object of the class
# -> not use the base class name explictly
# -> helps in working with multiple inheritances

class Class():
    def __init__(self):
        print(x)

class subClass(Class):
    def __init__(self, x):
        super.__init__(x)

x = [1, 2, 3, 4, 5]
a = subClass(x)

# 3. Method overloading:
# -> methods or functions have same name but different signature
# -> example of compiletime polymorphism
# -> no need of more than one class
# -> ingeritance may or may not be required

def add(datatype, *args):
    if datatype == "int":
        answer = 0

    if datatype == "str":
        answer = ""

    for x in args:
        answer = answer = x
    print(answer)

add("int", 5, 6)
add("str", "Hello", "World")

# 4. Method Overriding:
# -> methods and functions have same name and same signature
# -> example of runtime polymorphism
# -> need of atleast two classes
# -> inheritance always required

class A:
    def func1(self):
        print("Feature 1 of calss A")

    def func2(self):
        print("Feature 2 of calss A")

class B:
    def func1(self):
        print("Modified feature 1 of calss A by class B")

    def func3(self):
        print("Feature 3 of calss B")

obj = B
obj.func1()

# Task 4:
class Employee:
    def __init__(self):
        self.name = "Hello"
        self.add = self.add()

    def show(self):
        print("Name: ", self.name)

    class Address():
        def __init__(self):
            self.add = "India"

        def display(self):
            print("Add: ", self.add)
        
e1 = Employee()
e1.show()

# Task 5:
class calculator:

    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b
    
    @classmethod
    def mul(cls, a, b):
        return a * b
    
    @classmethod
    def div(cls, a, b):
        if b == 0:
            return "Error: Connot divide by zero"
        return a / b
    
print("Addition: ", calculator.add(10, 5))
print("Subtraction: ", calculator.sub(10, 5))
print("Multiplication: ", calculator.mul(10, 5))
print("Division: ", calculator.div(10, 5))