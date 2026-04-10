#pnadas is a powerful data manipulation library in Python. It provides data structures and functions needed to manipulate structured data seamlessly. The primary data structures in pandas are Series (1-dimensional) and DataFrame (2-dimensional).
#Pandas is widely used in data analysis, data cleaning, and data visualization tasks.

import pandas as pd #pd is an alias for pandas, which is a common convention in the Python community.

data = {
    "student_id": [1, 2, 3, 4, 5, 6],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "age": [20, 21, 19, 22, 20, 21],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "score": [85, 90, 78, 92, 88, 80]
}
df = pd.DataFrame(data)

def Section1(): #Creating a DataFrame from a dictionary
    # print(df) # prints the DataFrame
    print(df.head(2)) # prints the first 2 rows of the DataFrame
    print(df.tail(2)) # prints the last 2 rows of the DataFrame
    print(df.info()) # prints a concise summary of the DataFrame, including the data types
    print(df.shape) # prints the shape of the DataFrame (number of rows, number of columns)
    print(df.dtypes) # prints the data types of each column in the DataFrame

def Section2():
    print(df[["name", "score"]]) # prints the 'name' column of the DataFrame
    print(df.iloc[0]) # prints the first row of the DataFrame using integer-location based indexing

def Section3(): #Selecting columns and rows in a DataFrame
    selected_columns = df[df["Score"] > 85] # selects rows where the 'Score' column is greater than 85
    print(selected_columns)

def Section4(): #Updating operations in a DataFrame
    df["result"] = df["score"].where(df["score"] >= 85, "fail") # creates a new column 'result' based on the condition of the 'score' column
    df["result"] = df["result"].where(df["result"] == "fail", "pass") # updates the 'result' column to "Pass" if the score is greater than or equal to 85, and "Fail" otherwise
    print(df)

def Section5(): #Aggregation methods in a DataFrame
    print(df["score"].mean()) # calculates the mean of the 'score' column
    print(df["score"].sum()) # calculates the sum of the 'score' column
    print(df["score"].min()) # finds the minimum value in the 'score' column
    print(df["score"].max()) # finds the maximum value in the 'score' column
    
    print(df.sort_values(by = "score", ascending=False)) # sorts the DataFrame by the 'score' column in descending order

if __name__ == "__main__":
    # Section1()
    # Section2()
    # Section3()
    #Section4()
    # Section5()
    Section5()

#loading data from a CSV file into a DataFrame
# df = pd.read_csv("path_to_your_file.csv") # replace "path_to_your_file.csv" with the actual path to your CSV file
#it gives dataframe from the csv file, which can be used for further analysis and manipulation.
#loading data from an Excel file into a DataFrame
# df = pd.read_excel("path_to_your_file.xlsx") # replace "path_to