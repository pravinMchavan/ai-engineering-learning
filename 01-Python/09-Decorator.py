#Decorator is a design pattern in Python that allows you to modify the behavior of a function or class method without changing its source code. It is often used to add functionality to existing code in a clean and reusable way.
#A decorator in Python is a function that modifies another function without changing its code.
# import random
# def defrandomnumberGenerator(function):
#     def wrapper():
#         random_number = random.randint(1, 100)
#         function(random_number)
#     return wrapper

# @defrandomnumberGenerator
# def functionA(num):
#     print(f"Generated random number: {num}")

# @defrandomnumberGenerator
# def functionB(num):
#     print(f"Random number squared: {num}")

# @defrandomnumberGenerator
# def functionC(num):
#     print(f"Random number cubed: {num}")

# functionA()
# functionB()
# functionC()

# Passing Function as Argument
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        func(*args, **kwargs)
        print("After function")
    return wrapper

def say_hello(name):
    print(f"Hello, {name}!")

decorated = my_decorator(say_hello)
decorated("Alice")