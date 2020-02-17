# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 9-4


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
        self.number_served = 0

    def describe_restaurant(self):
        """
        Method that prints out the attributes of the restaurant.
        """
        print("Thank you for choosing, " + self.restaurant_name + ". Our soup of the day is " + self.cuisine_type +
              ". We hope you enjoy.")

    def open_restaurant(self):
        """
        Method that prints a message stating that the restaurant is open.
        """
        print(self.restaurant_name + " is now open. Please come sit and enjoy our food.")

    def set_number_served(self, guests):
        """
        Method that sets the number of guests that have come to the restaurant.
        :param guests: Passed arbitrary value of guests
        :return:
        """
        self.number_served = guests
        print(self.restaurant_name + " has had " + str(self.number_served) + " guests today!")

    def increment_number_served(self, guests):
        """
        Method that increments the number of guests that have come to the restaurant by a passed value
        :param guests: passed arbitrary value of guests
        :return:
        """
        self.number_served += guests
        print(self.restaurant_name + " has had " + str(self.number_served) + " guests come in and out today!")


restaurant = Restaurant('Jahrae\'s Kitchen', 'Goat Head Soup')

restaurant.open_restaurant()
restaurant.describe_restaurant()
restaurant.set_number_served(100)
restaurant.increment_number_served(20)
