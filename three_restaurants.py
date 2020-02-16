# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 9-2


class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
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
        print("Thank you for choosing, " + self.restaurant_name + ". Our special of the day is " + self.cuisine_type +
              ". We hope you enjoy.")

    def open_restaurant(self):
        """
        Method that prints a message stating that the restaurant is open.
        """
        print(self.restaurant_name + " is now open. Please come sit and enjoy our food.")


mcdonalds = Restaurant("McDonald\'s", "A McChicken")
burgerking = Restaurant("Burger King", "A Whopper Jr")
wendys = Restaurant("Wendy\'s", "Dave\'s Single")

wendys.describe_restaurant()
mcdonalds.describe_restaurant()
burgerking.describe_restaurant()
