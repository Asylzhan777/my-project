# Example 1: enumerate list
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Example 2: enumerate with start index
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Example 3: zip two lists
names = ["Alice", "Bob"]
scores = [90, 85]
print(list(zip(names, scores)))

# Example 4: iterate using zip
for name, score in zip(names, scores):
    print(name, score)

# Example 5: unzip pairs
pairs = [("a", 1), ("b", 2)]
letters, numbers = zip(*pairs)
print(letters)
print(numbers)