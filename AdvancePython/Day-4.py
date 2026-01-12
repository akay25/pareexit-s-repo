# Day 4: Modular Programming

# Task 1: Modules
# -> modules are like a code library
# -> to create a module file just save it with .py extension
# -> a file contains a set of functions which we want to include in the application

import module_file as mod

a = mod.person1["age"]
print(a)

# Task 2: Package
# -> it is like a container which contains various functions to perform specific task 
# -> package is a folder which contains multiple module files in it
# -> also a '__init__.py' file may empty but contain the package list

from math_operations import calculate, add, subtract, multiply, divide

calculate()

print("Addition: ", add(5, 2))
print("Multiplication: ", multiply(10, 4))

# Task 3: Decorators
# -> Decorators lets add extra behaviour to a function, without changing the function code
# -> it is a function that takes another function as input, and returns a function

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello World!"

print(myfunction())

# Task 4:
import module_task as module

a = module.square(5)
print(a)

# Task 5:
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time taken: {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@timer
def waste_time():
    time.sleep(1)
    print("Function finished!")
waste_time()