'''
generate a password that has a minimum of one uppercase, one lowercase, one digit and one special character.

'''
import random
import string
def random_password(size):
    all_chars = string.ascii_letters + string.digits
    password = ""
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.digits)
    for i in range(size - 3):
        password += random.choice(all_chars)
    return password

pass_len = int(input('what would be the password length: '))
print(random_password(pass_len))
