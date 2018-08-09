import random
chars ='abcdefghijklmnopqrstuvwxyz1234567890'
no_of_password = input("No. of password : ")
no_of_password = int(no_of_password)
length = input('password length : ')
length = int(length)

for p in range(no_of_password):
        password = ''
        for c in range(length):
             password += random.choice(chars)
        print(password)
