#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# This is to assign and store the characters that have been chosen randomly
password_list = []

# Making random choices for each type of char and assigning it to "password_list"
for x in range(nr_letters):
	password_list += random.choice(letters)

for x in range(nr_symbols):
	password_list += random.choice(symbols)

for x in range(nr_numbers):
	password_list += random.choice(numbers)

# Shuffle the list to get random order
random.shuffle(password_list)

# Unpacking the "password_list"
password = ""
for x in password_list:
	password += x


print(f"Your password is: {password}")
	 