#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#METHOD1 -  USING LISTS

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

list = []
for i in range(1, nr_letters + 1):
    # list.append (random.choice(letters))
    # WE CAN ALSO USE RANDOM.CHOICE DIRECTLY LIKE :
    list += random.choice(letters)
for i in range(1, nr_symbols + 1):
    list.append(random.choice(symbols))
for i in range(1, nr_numbers + 1):
    list.append(random.choice(numbers))
pwd = ''.join(map(str, list))  #converting list to string
print(f'''\nHere is your password: {pwd}''')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pwd_strong = ''
for i in range(1, len(pwd) + 1):
    #pwd_strong += ''.join(random.choice(''.join(map(str, list))))
    #pwd_strong += ''.join(random.choice(list))
    pwd_strong += ''.join(random.choice(pwd))
print(f'''\nHere is your strong password: {pwd_strong}''')

#METHOD2 -  USING STRINGS

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

empty_string = ''
for i in range(1, nr_letters + 1):
    empty_string += random.choice(letters)
for i in range(1, nr_symbols + 1):
    empty_string += random.choice(symbols)
for i in range(1, nr_numbers + 1):
    empty_string += random.choice(numbers)
print(f'''\n\nHere is your password: {empty_string}''')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pwd_strong_2 = ''
for i in range(1, len(empty_string) + 1):
    pwd_strong_2 += (random.choice(empty_string))
print(f'''\nHere is your strong password: {pwd_strong_2}''')

#METHOD3 -  USING RANDOM.SHUFFLE (can only be used on the list method and not string method)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

list2 = []
for i in range(1, nr_letters + 1):
    # list.append (random.choice(letters))
    # we can also use random.choice directly like :
    list2 += random.choice(letters)
for i in range(1, nr_symbols + 1):
    list2.append(random.choice(symbols))
for i in range(1, nr_numbers + 1):
    list2.append(random.choice(numbers))
pwd2 = ''.join(map(str, list))  #converting list to string
print(f'''\n\nHere is your password: {pwd2}''')
print("\nHere is the list ", (list2))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# USING THE RANDOM.SHUFFLE() FUNCTION
random.shuffle(list2)
pwd_strong2 = ''.join(list2)
print(f'''\nHere is your strong password: {pwd_strong2}''')


###THIS CODE WILL CHECK IF THE PASSWORD HAS SAME CHARACTERS OR NOT####
# password1 = "EgUp$))(+423604"  # Replace this with your first password
# password2 = "EgUp$))(+423604"  # Replace this with your second password

# # Check if the two passwords contain the same characters
# if sorted(password1) == sorted(password2):
#     print("The passwords contain the same characters.")
# else:
#     print("The passwords do not contain the same characters.")
