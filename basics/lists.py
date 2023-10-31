"""Lists"""
# A list stores a series of items in a particular order.
# Lists allow you to store sets of information in one
# place, whether you have just a few items or millions
# of items. Lists are one of Python's most powerful
# features readily accessible to new programmers, and
# they tie together many important concepts in
# programming.

# ---------------------    Creation/Getting   ---------------------

# Use square brackets to define a list, and use commas to
# separate individual items in the list.

# Making a list
users = ['val', 'bob', 'mia', 'ron', 'ned']

# Getting the first element
FIRST_USER = users[0]

# Getting the second element
SECOND_USER = users[1]

# Getting the last element
NEWEST_USER = users[-1]

# ---------------------    Modifying    ---------------------

# Changing an element
users[0] = 'valerie'
users[-2] = 'ronald'

# Adding an element to the end of the list
users.append('amy')

# Starting with an empty list
users = []
users.append('val')
users.append('bob')
users.append('mia')

# Inserting elements at a particular position
users.insert(0, 'joe')
users.insert(3, 'bea')

# Deleting an element by its position
del users[-3]

# Removing an item by its value
users.remove('mia')

# ---------------------    Pop    ---------------------

# Pop the last item from a list
most_recent_user = users.pop()
print(most_recent_user)

# Pop the first item in a list
FIRST_USER = users.pop(0)
print(FIRST_USER)

# ---------------------    Length    ---------------------

# Find the length of a list
NUM_USERS = len(users)
print("We have " + str(NUM_USERS) + " users.")

# ---------------------    Sorting    ---------------------

# The sort() method changes the order of a list permanently.
# The sorted() function returns a copy of the list, leaving the
# original list unchanged. You can sort the items in a list in
# alphabetical order, or reverse alphabetical order. You can
# also reverse the original order of the list. Keep in mind that
# lowercase and uppercase letters may affect the sort order.

users = ['val', 'bob', 'mia', 'ron', 'ned']

# Sorting a list permanently
users.sort()

# Sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)

# Sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse=True))

# Reversing the order of a list
users.reverse()

# ---------------------    Looping    ---------------------

# Printing all items in a list
for user in users:
    print(user)

# Printing a message for each item, and a separate message afterward
for user in users:
    print("Welcome, " + user + "!")

# You can use the range() function to work with a set of numbers efficiently.
# The range() function starts at 0 by default, and stops one number below the number passed to it.
# You can use the list() function to efficiently generate a large list of numbers.

# Printing the numbers 0 to 1000
for number in range(1001):
    print(number)

# Printing the numbers 1 to 1000
for number in range(1, 1001):
    print(number)

# Making a list of numbers from 1 to a million
numbers = list(range(1, 1000001))

# ---------------------    Simple Stats    ---------------------

# Finding the minimum value in a list
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)

# Finding the maximum value
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
oldest = max(ages)

# Finding the sum of all values
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
total_years = sum(ages)

# ---------------------    Slicing    ---------------------

# A portion of a list is called a slice.
# To slice a list start with the index of the first item you want,
# then add a colon and the index after the last item you want.
# Leave off the first index to start at the beginning of the list,
# and leave off the last index to slice through the end of the list.
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']

# Getting the first three items
first_three = finishers[:3]

# Getting the middle three items
middle_three = finishers[1:4]

# Getting the last three items
last_three = finishers[-3:]

# ---------------------    Copying    ---------------------

# To copy a list make a slice that starts at the first item and
# ends at the last item. If you try to copy a list without using
# this approach, whatever you do to the copied list will affect
# the original list as well.

# Making a copy of a list
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
copy_of_finishers = finishers[:]

# ---------------------    Comprehension    ---------------------

# To write a comprehension, define an expression for the
# values you want to store in the list. Then write a for loop to
# generate input values needed to make the list.

# Using a loop to generate a list of square numbers
squares = []
for x in range(1, 11):
    square = x ** 2
    squares.append(square)

# Using a comprehension to generate a list of square numbers
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# Using a loop to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())

# Using a comprehension to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]
