# A class defines the behavior of an object and the kind of
# information an object can store. The information in a class
# is stored in attributes, and functions that belong to a class
# are called methods. A child class inherits the attributes and
# methods from its parent class.

# Creating a dog class
class Dog:
    """Represent a dog."""

    def __init__(self, name):
        """Initialize dog object."""
        self.name = name

    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")


my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()


# Inheritance
class SARDog(Dog):
    """Represent a search dog."""

    def __init__(self, name):
        """Initialize the sardog."""
        super().__init__(name)

    def search(self):
        """Simulate searching."""
        print(self.name + " is searching.")


my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()
