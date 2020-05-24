# Agenda- User Input In Python
# Getting user Input
# In python we use input() function to get the user input.
# When input() function is executed it wait for the user to type something and press enter.
# you will get a string in return from input() function.
from datetime import date

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"{name} is {age} years old.")
print(type(name))
print(type(age))

age = int(age)  # Converting to int
print("\n ------------\n")
print(type(age))

#  Create a program that asks the user to enter their name and their age.
#  Print out a message addressed to them that tells them the year that they will turn 100 years old.
curr_year = date.today()
print(f"\n You will be 100yrs old on year: {(curr_year.year)-age + 100}")


