# List comprehension in Python is a compact and powerful way to create lists in a single line instead of writing multiple lines using loops.

# new_list = [expression for item in iterable]

# numbers = [1,2,3,4]
# square = [x*x for x in numbers] # x is the expression, x is the item, and numbers is the iterable. This will create a new list called square that contains the squares of the numbers in the original list.
# print(square)

# # List comprehension with condition (Filtering)

# #new_list = [expression for item in iterable if condition]
# numbers = [1,2,3,4,5,6]
# even_numbers = [x for x in numbers if x % 2 == 0] # This will create a new list called even_numbers that contains only the even numbers from the original list.
# print(even_numbers)

# List comprehension with if-else condition
# numbers = [1,2,3,4,]
# result = ["Even" if x % 2 == 0 else "odd" for x in numbers]
# print(result)

# List comprehension with matrix
# matrix = [[1,2,3], [4,5,6]]
# flattened = [num for row in matrix for num in row] # This will create a new list called flattened that contains all the numbers from the original matrix in a single list.
# print(flattened)