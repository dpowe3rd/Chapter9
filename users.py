# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 9-3


class User:
    """
    A model of a website user
    """

    def __init__(self, first_name, last_name, email, location, username):
        """
        Initialize attributes to describe a user and their profile.
        :param first_name: First name of user
        :param last_name:  Last name of user
        :param user_info: dictionary of a arbitrary amount potential arguments
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = self.first_name + " " + self.last_name
        self.email = email
        self.username = username
        self.location = location

    def describe_user(self):
        """Describes a user, based on their information"""
        print("\n " + self.full_name +":")
        print("\tUsername: " + self.username)
        print("\tEmail Address: " + self.email)
        print("\tLocation: " + self.location)

    def greet_user(self):
        print("Hello, " + self.username + ", how are you doing today?")


darrell = User('darrell', 'powe', 'ghadajna@gmail.com', 'Bronx, New York', 'dpowe96')
darrell.describe_user()
darrell.greet_user()

jahrae = User('jahrae', 'martinez', 'xfhdbc@gmail.com', 'Bronx, New York', 'jmartinez12')
jahrae.describe_user()
jahrae.greet_user()

keyante = User('keyante', 'hunter', 'ajhdch@gmail.com', 'Bronx, New York', 'khunter4456')
keyante.describe_user()
keyante.greet_user()