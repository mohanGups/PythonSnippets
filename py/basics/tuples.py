# Tuples

# A tuple is like a list, except you can't change the values in a tuple once it's defined.
# Tuples are good for storing information that shouldn't be changed throughout the life of
# a program. Tuples are designated by parentheses instead of square brackets.
# You can overwrite an entire tuple, but you can't change the individual elements in a tuple,

# Making a tuple
dimensions = (1920, 1080)

# Looping through a tuple
for dimension in dimensions:
    print(dimension)

# Overwriting a tuple
dimensions = (800, 600)
print(dimensions)
