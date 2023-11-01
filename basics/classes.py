# A class defines the behavior of an object and the kind of
# information an object can store. The information in a class
# is stored in attributes, and functions that belong to a class
# are called methods. A child class inherits the attributes and
# methods from its parent class.


# ---------------------    Creating and using   ---------------------

# Consider how we might model a car. What information
# would we associate with a car, and what behavior would it
# have? The information is stored in variables called
# attributes, and the behavior is represented by functions.
# Functions that are part of a class are called methods

# The Car class
class Car():
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")

    # [Attr Modification] Writing a method to update an attribute's value
    def update_fuel_level(self, new_level):
        """Update the fuel level."""
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")

    # [Attr Modification] Writing a method to increment an attribute's value
    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if self.fuel_level + amount <= self.fuel_capacity:
            self.fuel_level += amount
            print("Added fuel.")
        else:
            print("The tank won't hold that much.")


# Creating an object from a class
my_car = Car('audi', 'a4', 2016)

# Accessing attribute values
print(my_car.make)
print(my_car.model)
print(my_car.year)

# Calling methods
my_car.fill_tank()
my_car.drive()

# Creating multiple objects
my_car = Car('audi', 'a4', 2016)
my_old_car = Car('subaru', 'outback', 2013)
my_truck = Car('toyota', 'tacoma', 2010)

# ---------------------    Modifying Attributes  ---------------------

# You can modify an attribute's value directly, or you can
# write methods that manage updating values more carefully.

# Modifying an attribute directly
my_new_car = Car('audi', 'a4', 2016)
my_new_car.fuel_level = 5


# See the methods markd [Attr Modification] for other ways to modify attrs

# ---------------------    Inheritance    ---------------------

# A class can have objects as attributes. This allows classes
# to work together to model complex situations.
# A Battery class
class Battery():
    """A battery for an electric car."""

    def __init__(self, size=70):
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %.
        self.size = size
        self.charge_level = 0

    def get_range(self):
        """Return the battery's range."""
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270


# The __init__() method for a child class
class ElectricCar(Car):
    """A simple model of an electric car."""

    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)

        # Attributes specific to electric cars.
        # Standard attribute
        self.range = 70

        # Class instance attribute
        self.battery = Battery()

    # Adding new methods to the child class
    def update_range(self):
        self.range = 100

    def charge(self):
        """Fully charge the vehicle."""
        self.battery.charge_level = 100
        print("The vehicle is fully charged.")

    # Overriding parent methods
    def fill_tank(self):
        """Display an error message."""
        print("This car has no fuel tank!")


# Using child methods and parent methods
my_ecar = ElectricCar('tesla', 'model s', 2016)
my_ecar.update_range()
my_ecar.charge()
print(my_ecar.battery.get_range())
my_ecar.drive()

# ---------------------    Example    ---------------------

# A fleet of rental cars
# Make lists to hold a fleet of cars.
gas_fleet = []
electric_fleet = []

# Make 500 gas cars and 250 electric cars.
for _ in range(500):
    car = Car('ford', 'focus', 2016)
    gas_fleet.append(car)

for _ in range(250):
    car = ElectricCar('nissan', 'leaf', 2016)
    electric_fleet.append(car)

# Fill the gas cars, and charge electric cars.
for car in gas_fleet:
    car.fill_tank()

for car in electric_fleet:
    car.charge()

print("Gas cars:", len(gas_fleet))
print("Electric cars:", len(electric_fleet))
