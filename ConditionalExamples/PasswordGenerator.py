import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '!', '#', '%', '$']

print("Welcome to Py Password generator!!")
nr_letters = int(input("Enter how many letters do you want password to be?\n"))
nr_symbols = int(input("Enter how many symbols you want password should contain\n"))
nr_numbers = int(input("Enter how many numbers you want password to contain\n"))

password=""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print(password)
