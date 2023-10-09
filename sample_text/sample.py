# Wine Bar Monokai - Python Sample

# This is a Python code sample using the Wine Bar Monokai theme.

# Variables and Data Types
message = "Hello, Python!"
integer_number = 42
float_number = 3.14159
boolean_value = True

# Lists and Indexing
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]
last_fruit = fruits[-1]

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Conditional Statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loops
for fruit in fruits:
    print(fruit)

# Functions
def greet(name):
    return f"Hello, {name}!"

# Classes and Object-Oriented Programming
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking.")

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# File Handling
with open("sample.txt", "w") as file:
    file.write("This is a sample text file.")

# External Libraries
import numpy as np
import pandas as pd

# NumPy Arrays
array = np.array([1, 2, 3, 4, 5])

# Pandas DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}
df = pd.DataFrame(data)

# Conclusion
print("This Python code sample showcases the Wine Bar Monokai theme with various Python features.")
