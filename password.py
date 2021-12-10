#password generator
# made by SASNOKOV

import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910!%&*^@`~()[]{\|}12/?.,<>-+_"
while 1:
    password_length = int(input("How long is your password to be? : "))
    number_of_passwords = int(input("How many passwords would you like? : "))
    for x in range(0,number_of_passwords):
        password = ""
        for x in range(0,password_length):
            password_character = random.choice(
            characters)
            password      = password + password_character
        print("we present your password : ", password)
