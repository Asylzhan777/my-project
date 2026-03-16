import shutil

# Example 1: Move a file
shutil.move("file1.txt", "folder/file1.txt")

# Example 2: Rename a file using move
shutil.move("file2.txt", "renamed_file.txt")

# Example 3: Move file into another folder
shutil.move("file3.txt", "folder/")

# Example 4: Move a folder
shutil.move("old_folder", "new_folder")

# Example 5: Move and overwrite
shutil.move("file4.txt", "folder/file4.txt")