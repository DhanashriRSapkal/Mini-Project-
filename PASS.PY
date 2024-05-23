

import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

characters = list(lower + upper +num + symbols)

def generate_random_password():
       length = int(input("Enter password length: "))
       random.shuffle(characters)
       password = []
for i in range(length):
       password.append(random.choice(characters))
       random.shuffle(password)
       print("".join(password))


while True:
      generate_random_password()
