# Functions are named blocks of code, designed to do one
# specific job. Information passed to a function is called an
# argument, and information received by a function is called a
# parameter.

# ---------------------    Creation   ---------------------

# A simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()


# ---------------------    Arguments   ---------------------

# Passing an argument
def greet_user(username):
    """Display a personalized greeting."""
    print("Hello, " + username + "!")


greet_user('jesse')


# Using positional arguments
def describe_pet(animal, name):
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Using keyword arguments
describe_pet(animal='hamster', name='harry')
describe_pet(name='willie', animal='dog')


# Using a default value
def describe_pet(name, animal='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")


describe_pet('harry', 'hamster')
describe_pet('willie')


# Using None to make an argument optional
def describe_pet(animal, name=None):
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    if name:
        print("Its name is " + name + ".")


describe_pet('hamster', 'harry')
describe_pet('snake')


# ---------------------    Returning Values   ---------------------

# Returning a single value
def get_full_name(first, last):
    """Return a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()


musician = get_full_name('jimi', 'hendrix')
print(musician)


# Returning a dictionary
def build_person(first, last):
    """Return a dictionary of information
    about a person.
    """
    person = {'first': first, 'last': last}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# Returning a dictionary with optional values
def build_person(first, last, age=None):
    """Return a dictionary of information
    about a person.
    """
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', 27)
print(musician)
musician = build_person('janis', 'joplin')
print(musician)


# ---------------------    Lists as args, pass by value & pass by ref   ---------------------

# Passing a list as an argument
def greet_users(names):
    """Print a simple greeting to everyone."""
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# Allowing a function to modify a list
# The following example sends a list of models to a function for
# printing. The original list is emptied, and the second list is filled.
def print_models(up, p):
    """3d print a set of models."""
    while up:
        current_model = up.pop()
        print("Printing " + current_model)
        p.append(current_model)


# Store some unprinted designs, and print each of them.
unprinted = ['phone case', 'pendant', 'ring']
printed = []
print_models(unprinted, printed)

print("\nUnprinted:", unprinted)
print("Printed:", printed)

# Preventing a function from modifying a list
# The following example is the same as the previous one, except the
# original list is unchanged after calling print_models().

original = ['phone case', 'pendant', 'ring']
printed = []

# shorthand way to pass list by value
print_models(original[:], printed)
print("\nOriginal:", original)
print("Printed:", printed)


# ---------------------    Arbitrary number of args   ---------------------

# Sometimes you won't know how many arguments a
# function will need to accept. Python allows you to collect an
# arbitrary number of arguments into one parameter using the
# * operator. A parameter that accepts an arbitrary number of
# arguments must come last in the function definition.
# The ** operator allows a parameter to collect an arbitrary
# number of keyword arguments.

# Collecting an arbitrary number of arguments
def make_pizza(size, *toppings):
    """Make a pizza."""
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)


# Make three pizzas with different toppings.
make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers',
           'onions', 'extra cheese')


# Collecting an arbitrary number of keyword arguments
def build_profile(first, last, **user_info):
    """Build a user's profile dictionary."""
    # Build a dict with the required keys.
    profile = {'first': first, 'last': last}
    # Add any other keys and values.
    for key, value in user_info.items():
        profile[key] = value
    return profile


# Create two users with different kinds
# of information.
user_0 = build_profile('albert', 'einstein', location='princeton')
user_1 = build_profile('marie', 'curie', location='paris', field='chemistry')
print(user_0)
print(user_1)
