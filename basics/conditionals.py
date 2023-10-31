# If statements are used to test for particular conditions and
# respond appropriately.

# Conditional tests
x = 1

# equals
x == 42

# not equal
x != 42

# greater than or equal to
x > 42
x >= 42

# less than or equal to
x < 42
x <= 42

# Conditional test with lists
bikes = ['trek', 'specialized']
'trek' in bikes
'surly' not in bikes

# Assigning boolean values
game_active = True
can_edit = False

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
