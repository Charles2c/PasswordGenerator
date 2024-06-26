import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbol = list(string.punctuation)

def passwordGenerator():
    length = int(input("Enter Length of Password: "))

    letters_count = int(input("Letter Count: "))
    numbers_count = int(input("Number Count: "))
    symbol_count = int(input("Symbol Count: "))

    characters_count = letters_count + numbers_count + symbol_count

    if characters_count != length:
        print("Character count is not equal to length of password")
        print(letters_count + numbers_count + symbol_count, "is the total you currently have")
        print(length, "is your chosen length")
        return

    password = []

    for i in range(letters_count):
        password.append(random.choice(letters))

    for i in range(numbers_count):
        password.append(random.choice(numbers))

    for i in range(symbol_count):
        password.append(random.choice(symbol))

    random.shuffle(password)
    print("".join(password))

passwordGenerator()