"""Conditionals"""

# If statements are used to test for particular conditions and
# respond appropriately.

# ---------------------    Fundamentals   ---------------------

# Conditional tests
x = 1

# equals
print(x == 42)

# not equal
print(x != 42)

# greater than or equal to
print(x > 42)
print(x >= 42)

# less than or equal to
print(x < 42)
print(x <= 42)

# Assigning boolean values
game_active = True
CAN_VOTE = True

# A simple if test
age = 30
if age >= 18:
    print("You can vote!")

# If-elif-else statements
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15

# and/or
if age >= 18 or age <= 65:
    print("Can work")

if age >= 18 and CAN_VOTE:
    print("Can vote")

# Simplified chain
if 18 <= age <= 65:
    print("Can work")

# ---------------------    With Lists   ---------------------

# Conditional test with lists
bikes = ['trek', 'specialized']
print('trek' in bikes)
print('surly' not in bikes)

# Testing if a value is not in a list
banned_users = ['ann', 'chad', 'dee']
user = 'erin'
if user not in banned_users:
    print("You can play!")

# Checking if a list is empty
players = []
if players:
    for player in players:
        print("Player: " + player.title())
else:
    print("We have no players yet!")
