from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Example 1: map - multiply by 2
result = list(map(lambda x: x * 2, numbers))
print(result)

# Example 2: map with function
def square(x):
    return x * x

print(list(map(square, numbers)))

# Example 3: filter even numbers
print(list(filter(lambda x: x % 2 == 0, numbers)))

# Example 4: filter numbers greater than 3
print(list(filter(lambda x: x > 3, numbers)))

# Example 5: reduce to sum numbers
print(reduce(lambda a, b: a + b, numbers))