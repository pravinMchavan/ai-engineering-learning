import os
print(os.getcwd())

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError: 
        print("File not Found")
        

def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Written successfully")
    except FileNotFoundError:
        print("File not found")


def append_to_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
        print(f"Content appended to '{file_name}' successfully.")
    except FileNotFoundError:
        print("File not found")


def copy_binary_file(source_file, destination_file):
    try:
        with open(source_file, 'rb') as src, open(destination_file, 'wb') as dst:
            content = src.read()
            dst.write(content)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Source file not found")


# Usage
file_name = file_name = r"C:\Pravin\Course\ai-engineering-learning\01-Python\07-Example.txt"

content = "Hello, this is a sample text file.\nThis file is used for demonstrating file handling in Python.\n"
content2 = "This is an additional line to be appended to the file.\n"

# append_to_file(file_name=file_name, content=content)
# append_to_file(file_name=file_name, content=content2)

filename_binary = r"C:\Pravin\Course\ai-engineering-learning\01-Python\08-Example.jpg"

destination_file = r"C:\Pravin\Course\ai-engineering-learning\01-Python\copy.jpg" # this file will be created if it doesn't exist

copy_binary_file(filename_binary, destination_file)