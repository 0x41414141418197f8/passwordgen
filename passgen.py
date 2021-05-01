import random

chars = "abcdefghijklmnopqrstuwxyzABCEFGHIJKLMNOPQRSTUVWXYZ1234567890#!\{}|-_=%^$*:/.(`)"

if 1:
    password_len = int(input("What length would you like ? : "))
    password_count = int(input("How many password you would ? :"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password :", password)