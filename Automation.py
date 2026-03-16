import os

# Create file
with open("sample.txt", "w") as file:
    file.write("This file was generated automatically.\n")

# Read file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# List files in directory
print("Files in current directory:")
print(os.listdir())