# # # Numpy is a powerful library for numerical computing in Python. 
# # # It provides support for large, multi-dimensional arrays and matrices,
# # # along with a collection of mathematical functions to operate on these arrays efficiently. 
# # # Numpy is widely used in data science, machine learning, and scientific computing.


import numpy as np #np is an alias for numpy, which is a common convention in the Python community.

# # # Creating a Numpy array from a Python list
# # my_list = [1, 2, 3, 4, 5]
# # print(my_list)

# # #2d array in numpy
# # #zeros matrix
# # zeros_matrix = np.zeros((3, 4)) # creates a 3x4 matrix filled with zeros
# # print(zeros_matrix) 

# # #ones matrix
# # ones_matrix = np.ones((2,3)) # creates a 2x3 matrix filled with ones
# # print(ones_matrix)

# # #arange function
# # # The arange function is used to create an array with evenly spaced values within a specified range. 
# # # It takes three parameters: start, stop, and step.
# # # The start parameter is the value at which the sequence starts (inclusive), the stop parameter is the value at which the sequence ends (exclusive), and the step parameter is the
# # # increment between each value in the sequence.
# # arange_array = np.arange(0, 10, 2) # creates an array of even numbers from 0 to 8
# # print(arange_array) #last value is exclusive, so 10 is not included in the array.

# # def section1(): #Creating a Numpy array from a Python list
# #     arr = np.array([[1,2,3],[4,5,6]]) # creates a 2D array (matrix) from a list of lists
# # if __name__ == "__main__": # This line checks if the script is being run directly (as the main program) rather than imported as a module in another script. 
# #     section1()

# #converting a float array to an integer array
# float_array = np.array([1.5, 2.3, 3.7]) # creates a 1D array of floats
# int_array = float_array.astype(int) # astype converts the float array to an integer array by truncating the decimal part
# print(int_array) 

# #check data type of the array
# print(int_array.dtype) # prints the data type of the elements in the int_array, which should be 'int32' or 'int64' depending on the system.
# #check size of the array
# print(int_array.size) # prints the number of elements in the int_array, which should be
# #check shape of the array
# print(int_array.shape) # prints the shape of the int_array, which should be (3
# #check number of dimensions of the array
# print(int_array.ndim) # prints the number of dimensions of the int_array, which should

def section3(): #indexing and slicing in numpy arrays
    array_1d = np.array([10, 20, 30, 40, 50]) # creates a 1D array
    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # creates a 2D array (matrix)
    print(array_1d[0]) # prints the first element of the 1D
    print(array_1d[1:4]) # prints a slice of the 1D array from index 1 to 3 (4 is exclusive)
    print(array_2d[1, 2]) # prints the element at row 1, column 2 of the 2D array
    print(array_2d[0:2, 1:3]) # prints a slice of the 2D array from rows 0 to 1 and columns 1 to 2 (3 is exclusive)
    print(array_2d[:, 0]) # prints all rows of the first column of the 2D array

def section4(): #aggregation methods
    arr = np.array([[1,2,3],[4,5,6]])
    print(arr.sum()) # calculates the sum of all elements in the array
    print(arr.mean())# calculates the mean (average) of all elements in the array
    print(arr.min()) # finds the minimum value in the array
    print(arr.max()) # finds the maximum value in the array 
    print(np.round(arr.std(), 4)) # calculates the standard deviation of all elements in the array, which measures the amount of variation or dispersion from the mean.


if __name__ == "__main__":
    # section3()
    section4()