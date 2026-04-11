#matplotlib is a plotting library for python
import matplotlib.pyplot as plt
import numpy as np

def section1():
    #plot a line graph
    x = [1,2,3,4,5]
    y = [1,4,9,16,25]
    plt.figure(figsize=(10,5)) #set the size of the figure
    plt.plot(x,y) #plot the line graph
    plt.title("Line Graph") #set the title of the graph
    plt.xlabel("X-axis")#set the label of the x-axis
    plt.ylabel("Y-axis")#set the label of the y-axis
    plt.show() #display the graph

def section2():
    #plot a line graph with customizations
    x = np.linspace(0,6) #create an array of 100 values between 0 and 10
    y = x**2 #create an array of the squares of the x values
    plt.figure(figsize=(7,4)) #set the size of the figure
    plt.plot(x,y, color='red', linestyle='--', linewidth=2, marker='o', markersize=6, markevery=10) #plot the line graph with customizations
    plt.title("Line Graph") #set the title of the graph
    plt.xlabel("X-axis")#set the label of the x-axis
    plt.ylabel("Y-axis")#set the label of the y-axis
    plt.grid(True) #display a grid
    plt.show() #display the graph

def section3():
    #plot multiple lines on the same graph
    x = np.linspace(0,2*np.pi,200) #create an array of 100 values between 0 and 2*pi
    y1 = np.sin(x) #create an array of the sine of the x values
    y2 = np.cos(x) #create an array of the cosine of the x values
    plt.figure(figsize=(10,5)) #set the size of the figure
    plt.plot(x,y1, label='sin(x)', color='blue', linewidth=2) #plot the sine graph
    plt.plot(x,y2, label='cos(x)', color='red', linewidth=2) #plot the cosine graph
    plt.title("Trigonometric Functions values") #set the title of the graph
    plt.xlabel("X-axis")#set the label of the x-axis
    plt.ylabel("Y-axis")#set the label of the y-axis
    plt.grid(True) #display a grid
    plt.legend() #display the legend
    plt.show() #display the graph

def section4():
    #plot a scatter graph
    np.random.seed(42) #set the random seed for reproducibility
    x = np.random.normal(50, 10, 100) #create an array of 100 random values from a normal distribution
    y = x * 2 + np.random.normal(0, 10, 100) #create an array of 100 random values from a normal distribution
    plt.figure(figsize=(7,4)) #set the size of the figure
    plt.scatter(x,y, color='green', marker='x', alpha=0.8) #plot a scatter graph
    plt.title("Scatter Graph") #set the title of the graph
    plt.xlabel("X-axis")#set the label of the x-axis
    plt.ylabel("Y-axis")#set the label of the y-axis
    plt.grid(True) #display a grid
    plt.show() #display the graph

def section5():
    #plot a bar graph
    categories = ['A', 'B', 'C', 'D', 'E'] #create a list of categories
    values = [10, 15, 7, 12, 20] #create a list of values
    plt.figure(figsize=(7,4)) #set the size of the figure
    plt.bar(categories, values, color='orange') #plot a bar graph
    plt.title("Bar Graph") #set the title of the graph
    plt.xlabel("Categories")#set the label of the x-axis
    plt.ylabel("Values")#set the label of the y-axis
    plt.grid(axis='y') #display a grid only on the y-axis
    plt.show() #display the graph

def section6():
    #plot a histogram
    np.random.seed(42) #set the random seed for reproducibility
    data = np.random.normal(0, 1, 1000) #create an array of 1000 random values from a normal distribution
    plt.figure(figsize=(7,4)) #set the size of the figure
    plt.hist(data, bins=30, color='purple', alpha=0.7) #plot a histogram
    plt.title("Histogram") #set the title of the graph
    plt.xlabel("Value")#set the label of the x-axis
    plt.ylabel("Frequency")#set the label of the y-axis
    plt.grid(True) #display a grid
    plt.show() #display the graph

if __name__ == "__main__":
    #section1()
    #section2()
    #section3()
    #section4()
    #section5()
    section6()
