import random

chars = "abcdefghijklmnopqrstuwxyzABCEFGHIJKLMNOPQRSTUVWXYZ1234567890#!\{}|-_=%^$*:/.(`)"
chars2 = "+#^@#%$+_-$=%=@+!@!#@+-_*-=--@!!$*=$*%^-@=*&**+@*#=_++-!^@===%^&==!=&$%_-_%-_+#*#_#=_@*&*@*++%!!^_*!"

if 1:
    password_length = int(input("What length would you like ? : "))
    password_c = int(input("How many password you would ? :"))
    for x in range(0,password_c):
        password = ""
        for x in range(0,password_length):
            password_char = random.choice(chars + chars2)
            password = password + password_char
        print(password)

