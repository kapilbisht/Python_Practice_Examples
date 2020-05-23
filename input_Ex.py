# Agenda- User Input In Python
# Getting user Input
# In python we use input() function to get the user input.
# When input() function is executed it wait for the user to type something and press enter.
# you will get a string in return from input() function.


name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"{name} is {age} years old.")
print(type(name))
print(type(age))

new_age = int(age)  # Converting to int
print("\n ------------\n")
print(type(new_age))

