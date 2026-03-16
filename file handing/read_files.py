# Example 1: Read the whole file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Example 2: Read file line by line
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

# Example 3: Read the first line
with open("example.txt", "r") as f:
    print(f.readline())

# Example 4: Read all lines into a list
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# Example 5: Read first 10 characters
with open("example.txt", "r") as f:
    print(f.read(10))