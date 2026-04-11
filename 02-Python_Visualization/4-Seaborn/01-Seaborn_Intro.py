#Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
#Seaborn is built on top of Matplotlib and integrates closely with pandas data structures. It provides a variety of functions for creating different types of plots, such as scatter plots, bar plots, histograms, and more. Seaborn also includes features for visualizing the distribution of data, relationships between variables, and categorical data.
#To use Seaborn, you need to install it first. You can do this using
#pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme (style="whitegrid") #Set the theme for the plots to "whitegrid"

def Section1():
    x = np.arange(1,11)
    y = np.array([20,22,25,30,28,35,40,38,45,50])

    plt.figure(figsize=(10,6))
    sns.lineplot(x=x,y=y, markers="o", markersize=8)
    plt.title("Line Plot")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()

def Section2():
    #scatter plot using seaborn
    np.random.seed(42)
    hours_studied = np.random.uniform(0, 10, 80)
    test_scores = 50 + hours_studied * 6 + np.random.normal(0, 5, 80)

    plt.figure(figsize=(10,6))
    sns.scatterplot(x=hours_studied, y=test_scores)
    plt.title("Scatter Plot")
    plt.xlabel("Hours Studied")
    plt.ylabel("Test Scores")
    plt.show()

def Section3():
    #histogram using seaborn
    np.random.seed(42)
    data = np.random.normal(loc=70, scale=10, size=300)

    plt.figure(figsize=(10,6))
    sns.histplot(x = data, bins=30, kde=True)
    plt.title("Histogram with KDE")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

def Section4():
    #box plot using seaborn
    np.random.seed(42)
    group_a = np.random.normal(loc=70, scale=10, size=100)
    group_b = np.random.normal(loc=75, scale=12, size=100)
    group_c = np.random.normal(loc=80, scale=8, size=100)
    data = [group_a, group_b, group_c]
    plt.figure(figsize=(10,6))
    sns.boxplot(data=data)
    plt.title("Box Plot")
    plt.xlabel("Group")
    plt.ylabel("Value")
    plt.show()

def section5():
    #bar plot using seaborn
    departments = ['HR', 'Finance', 'IT', 'Marketing']
    employees = [25, 40, 60, 35]    
    plt.figure(figsize=(10,6))
    sns.barplot(x=departments, y=employees)
    plt.title("Bar Plot")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")
    plt.show()

if __name__ == "__main__":
    #Section1()
    #Section2()
    #Section3()
    #Section4()
    section5()