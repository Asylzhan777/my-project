import shutil
import os

# Example 1: Copy a file
shutil.copy("file1.txt", "file_copy.txt")

# Example 2: Copy with metadata
shutil.copy2("file1.txt", "file_copy2.txt")

# Example 3: Delete a file
if os.path.exists("file_copy.txt"):
    os.remove("file_copy.txt")

# Example 4: Check if file exists
if os.path.exists("file1.txt"):
    print("File exists")

# Example 5: Rename a file
os.rename("file_copy2.txt", "renamed_file.txt")