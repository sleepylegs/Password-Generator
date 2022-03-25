import random

# intro to password generator
print('This is a password generator')
print('Over here you will have the option to choose the best type of password for you!')
print('==-==-==-==--==')

# password options
print('\nHere are your options:')
print('Option 1 - password with only letters')
print('Option 2 - password with only numbers')
print('Option 3 - password with both numbers and letters (much stronger option)')

# intructions to help users navigate and use the password manager
print('\n*For choosing option 1 press 1 and enter')
print('*For choosing option 2 press 2 and enter')
print('*For choosing option 3 press 3 and enter')

# actual password manager
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
mix = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# type of password
your_new_password = input(
    "\nWhat type of password would you like to have today: ")

# number of passwords the person wants to generate
print('\nType the deignated number for the amount of passwords you would like to generate at the same time:')
amt = input('How many passwords would you like to generate?: ')
amt = int(amt)

# length of the passwords the person wants to generate
print('\nType the deignated number for the amount of characters you would like to have in your password')
length = input('What would you like the length of your password to be?: ')
length = int(length)

# letter type of password
if your_new_password == "1":
    for psd in range(amt):
        passwords = ''
        for x in range(length):
            passwords += random.choice(letters)
        print('Here is a password:', passwords)

# number type of password
if your_new_password == "2":
    for psd in range(amt):
        passwords = ''
        for x in range(length):
            passwords += random.choice(numbers)
        print('Here is a password:', passwords)

# mix type of password
if your_new_password == "3":
    for psd in range(amt):
        passwords = ''
        for x in range(length):
            passwords += random.choice(letters+numbers)
        print('Here is a password:', passwords)
