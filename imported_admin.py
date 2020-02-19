# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 9-11 -- This is 1 half of the program

from imported_admin_modules import Admin


def main():
    darrell = Admin('darrell', 'powe', 'ghadajna@gmail.com', 'Bronx, New York', 'dpowe96')
    darrell.greet_admin()
    darrell.admin_power()
    darrell.privilege.show_privileges()


main()
