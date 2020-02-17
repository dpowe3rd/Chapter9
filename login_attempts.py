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
        :param email: Email address of user
        :param location: Location of user
        :param username: Username
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = self.first_name + " " + self.last_name
        self.email = email
        self.username = username
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Describes a user, based on their information"""
        print("\n " + self.full_name + ":")
        print("\tUsername: " + self.username)
        print("\tEmail Address: " + self.email)
        print("\tLocation: " + self.location)

    def greet_user(self):
        print("Hello, " + self.username + ", how are you doing today?")

    def increment_login_attempts(self):
        """
         Method that takes the login_attempts attribute and increments it by 1
        :return:
        """
        remaining_attempts = 2 - self.login_attempts
        self.login_attempts += 1
        print(str(self.login_attempts) + " login attempt(s) have been done so far. You have " + str(remaining_attempts)
              + " remaining attempt(s).")

        if remaining_attempts <= 0:
            print("You have no more login attempts. Please reset your password.")

    def reset_login_attempts(self):
        """
        Method that takes the login_attempts attribute and resets it to 0
        :return:
        """
        self.login_attempts = 0
        print("You\'re login attempts have been reset to " + str(self.login_attempts) + ".")


darrell = User('darrell', 'powe', 'ghadajna@gmail.com', 'Bronx, New York', 'dpowe3')
darrell.describe_user()
print("\n")
darrell.increment_login_attempts()
darrell.increment_login_attempts()
darrell.increment_login_attempts()
darrell.reset_login_attempts()
print("\n")
darrell.greet_user()
