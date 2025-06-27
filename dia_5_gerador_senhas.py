
import random

letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!@#$%&*()")

print("WELCOME TO THE PASSWORD GENERATOR")
hm_letters = int(input("HOW MANY LETTERS WOULD YOU LIKE? "))
hm_symbols = int(input("HOW MANY SYMBOLS WOULD YOU LIKE? "))
hm_numbers = int(input("HOW MANY NUMBERS WOULD YOU LIKE? "))

password = []

for _ in range(hm_letters):
    password.append(random.choice(letters))

for _ in range(hm_symbols):
    password.append(random.choice(symbols))

for _ in range(hm_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

final_password = "".join(password)
print("YOUR PASSWORD IS:", final_password)
