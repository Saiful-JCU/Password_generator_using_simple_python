'''
Generate a password. your password may contain letters in uppercase or lowercase. It also may contain digits or special
characters.
'''

import  string
import random

def generate_password(size):
    all_chars = string.ascii_letters + string.digits 
    password = ''
    for char in range(size):
        rand_char = random.choice(all_chars)
        password = password + rand_char
    return password

pass_len = int(input('how many characters: '))
print(generate_password(pass_len))