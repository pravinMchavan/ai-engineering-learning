#Lambda functions are anonymous functions that can be defined in a single line of code. 
# They are often used for short, simple functions that are not intended to be reused elsewhere in the code.
# The syntax for a lambda function is as follows:
# lambda arguments: expression
# Here, `arguments` are the parameters that the function takes, and `expression` is
# the single expression that the function evaluates and returns.
# For example, you can create a lambda function to add two numbers like this:

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

multiply = lambda x, y: x * y
print(multiply(5, 3))  # Output: 15

# Lambda functions can also be used with higher-order functions like `map()`, `filter()`, and `reduce()`.
# For example, you can use a lambda function with `map()` to square a list of numbers:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
# You can also use a lambda function with `filter()` to filter out even numbers from a list:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# Lambda functions are a convenient way to create small, one-off functions without the need for a full function definition. However, for more complex functions or when code readability is a concern, it is often better to use a regular function definition with the `def` keyword.
