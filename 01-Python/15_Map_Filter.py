#Filter is a built-in function in Python that allows you to filter elements from an iterable (like a list) based on a specified condition. 
# It takes two arguments: a function that defines the condition and an iterable to filter.
# The function should return `True` for elements that you want to keep and `False` for elements that you want to discard.
# The `filter()` function returns an iterator that contains only the elements from the original iterable that
# satisfy the condition defined by the function. You can convert this iterator into a list or other iterable type if needed.
# For example, you can use `filter()` to filter out even numbers from a list:

import functools
#filter even numbers from a list
mylist = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, mylist))
print(even_numbers)  # Output: [2, 4, 6]

# Square the numbers in a list using map
squared_numbers = list(map(lambda x: x ** 2, mylist))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]

#sum of numbers in a list using reduce
sum_of_numbers = functools.reduce(lambda x, y: x + y, mylist)

print(sum_of_numbers)  # Output: 21
