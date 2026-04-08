# # new_dict = {key: value for item in iterable}
# # Dictionary comprehension in Python is a concise way to create dictionaries in a single line of code. It allows you to generate a new dictionary by applying an expression to each item in an iterable.

# #basic example

# numbers = [1, 2, 3, 4]
# square_dict = {x: x*x for x in numbers}
# print(square_dict)

# # if condition in dictionary comprehension

# numbers = [1, 2, 3, 4]

# result = {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}

# print(result)

# loop through a string and create a dictionary with the character as the key and its frequency as the value

student_marks = {"A": 80, "B": 40, "C": 70}

passed = {k: v for k, v in student_marks.items() if v >= 50}

print(passed)