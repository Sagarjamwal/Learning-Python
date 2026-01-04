import random
import string
#python has all the letters built in in string
letters=string.ascii_letters
numbers=string.digits
symbols="!@#$%^&*"

all=letters+numbers+symbols
password=""

length=int(input("Enter the desired password length: \n"))

for i in range(length):
    password+= random.choice(all)

print(f"Your Strong Password is {password}")