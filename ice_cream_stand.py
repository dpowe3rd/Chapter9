# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 9-6


class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type=""):
        """
        Initialize attributes to describe a restaurant.
        :param restaurant_name: Name of restaurant.
        :param cuisine_type: Type of cuisine.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """
        Method that prints out the attributes of the restaurant.
        """
        if self.cuisine_type != "":
            print("Thank you for choosing, " + self.restaurant_name + ". Our soup of the day is " + self.cuisine_type +
                  ". We hope you enjoy.")
        else:
            print("Welcome to " + self.restaurant_name + ", come on in!")

    def open_restaurant(self):
        """
        Method that prints a message stating that the restaurant is open.
        """
        print(self.restaurant_name + " is now open. Please come in.")


class IceCreamStand(Restaurant):
    """Models a ice cream stand and inherits from the restaurant class above"""

    def __init__(self, restaurant_name):
        """
        Initialize attributes to describe a Ice Cream Stand
        :param restaurant_name: Name of shop
        """
        super().__init__(restaurant_name)
        self.ice_cream_stand = restaurant_name
        self.flavors = ["vanilla", "chocolate", "strawberry", "mint-chip", "rocky road", "sherbet", ]

    def list_flavors(self):
        """
        Prints a list of flavors that the shop sells
        :return:
        """
        print("\nHere at " + self.ice_cream_stand + ", we sell:")
        for ice_cream_flavors in self.flavors:
            print("\t" + ice_cream_flavors.title())
        print("\nPlease take your pick!")


ice_cream = IceCreamStand('Jahrae\'s Cones & More!')
ice_cream.open_restaurant()
ice_cream.describe_restaurant()
ice_cream.list_flavors()
