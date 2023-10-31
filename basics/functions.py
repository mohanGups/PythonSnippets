# Functions are named blocks of code, designed to do one
# specific job. Information passed to a function is called an
# argument, and information received by a function is called a
# parameter.
# A simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()


# Passing an argument
def greet_user(username):
    """Display a personalized greeting."""
    print("Hello, " + username + "!")


greet_user('jesse')


# Default values for parameters
def make_pizza(topping='bacon'):
    """Make a single-topping pizza."""
    print("Have a " + topping + " pizza!")


make_pizza()
make_pizza('pepperoni')


# Returning a value
def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y


total = add_numbers(3, 5)
# note: sum is a built-in keyword and should be avoided
print(total)
