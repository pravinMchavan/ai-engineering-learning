# A generator is a special type of function that:
# 👉 returns values one by one (lazy execution)
# 👉 uses yield instead of return

# def gen():
#     yield 1

# print(gen())   # <generator object>

# # To get the values from the generator, we can use the next() function or a loop.   
# def gen():
#     yield 1 #yield is used to produce a value and pause the function's execution, allowing it to be resumed later. When the generator is resumed, it continues from where it left off, rather than starting over from the beginning of the function.
#     yield 2
#     yield 3

# g = gen()

# print(next(g))  # 1  # The next() function is used to retrieve the next value from the generator. Each time next() is called, the generator resumes execution until it reaches the next yield statement, at which point it returns the yielded value and pauses again. If there are no more values to yield, a StopIteration exception is raised.
# print(next(g))  # 2
# print(next(g))  # 3

# # Using a loop to get values from the generator
# def gen():
#     yield 1
#     yield 2
#     yield 3

# for i in gen():
#     print(i)

def calnumGenerator(num):
    for i in range(num):
        val = i * i
        yield val

for i in calnumGenerator(10):
    print(i)

