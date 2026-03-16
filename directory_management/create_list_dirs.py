import os

# Example 1: Create a directory
os.mkdir("new_folder")

# Example 2: Create nested directories
os.makedirs("parent_folder/child_folder")

# Example 3: List files and folders
print(os.listdir("."))

# Example 4: Check if directory exists
print(os.path.isdir("new_folder"))

# Example 5: Get current working directory
print(os.getcwd())