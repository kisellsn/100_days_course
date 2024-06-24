import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# res_letters = ""
# res_symbols = ""
# res_numbers = ""
# for i in range(nr_letters):
#     res_letters += random.choice(letters)
# for i in range(nr_symbols):
#     res_symbols += random.choice(symbols)
# for i in range(nr_numbers):
#     res_numbers += random.choice(numbers)
#
# # password = res_letters + res_symbols + res_numbers
# password = ''
#
#
# while res_letters or res_symbols or res_numbers:
#     ch = random.randint(0, 3)
#     if ch == 0 and res_letters!='':
#         password += res_letters[-1]
#         res_letters = res_letters[:-1]
#     if ch == 1 and res_symbols != '':
#         password += res_symbols[-1]
#         res_symbols = res_symbols[:-1]
#     if ch == 2 and res_numbers!='':
#         password += res_numbers[-1]
#         res_numbers = res_numbers[:-1]
password = []
for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_symbols):
    password.append(random.choice(symbols))
for i in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
password = "".join(password)
print(f"Your password = {password}")