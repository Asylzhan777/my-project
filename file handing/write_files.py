# Example 1: Write text to file
with open("output.txt", "w") as f:
    f.write("Hello World")

# Example 2: Write multiple lines
with open("output.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3")

# Example 3: Append text
with open("output.txt", "a") as f:
    f.write("\nThis line was appended")

# Example 4: Write list of lines
lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# Example 5: Write numbers using loop
with open("numbers.txt", "w") as f:
    for i in range(5):
        f.write(str(i) + "\n")