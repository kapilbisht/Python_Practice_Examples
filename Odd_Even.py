#  Ask user for number, depending on which print the message whether the number is odd or even.
number = int(input("Enter a number: "))
if number == 0:
    print('You have entered zero!!! Try another time.')
else:
    if number % 2 == 0:
        print(f'The number {number} is even.')
    else:
        print(f'The number {number} is odd.')
