# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 9-7


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

    def describe_user(self):
        """Describes a user, based on their information"""
        print("\n " + self.full_name + ":")
        print("\tUsername: " + self.username)
        print("\tEmail Address: " + self.email)
        print("\tLocation: " + self.location)

    def greet_user(self):
        print("Hello, " + self.username + ", how are you doing today?")


class Admin(User):
    """Models a admin of a website with privileges"""
    def __init__(self, first_name, last_name, email, location, username):
        super(Admin, self).__init__(first_name, last_name, email, location, username)
        self.privilege = Privileges()

    def greet_admin(self):
        print("Welcome back administrator, " + self.username + ". How are you doing today?")

    def admin_power(self):
        print("As an administrator, " + self.first_name.title() + ", you can do the following: ")


class Privileges:
    def __init__(self):
        self.privileges = ["Add a post", "Modify a post", "Delete a post", "Ban a User", "Unban a user",
                           "Kick user from chat", ]

    def show_privileges(self):

        for privileges in self.privileges:
            print("\t" + privileges)


darrell = Admin('darrell', 'powe', 'ghadajna@gmail.com', 'Bronx, New York', 'dpowe96')
darrell.greet_admin()
darrell.admin_power()
darrell.privilege.show_privileges()
