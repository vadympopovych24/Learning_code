import random
import string

password = ''
ch = string.ascii_letters + string.digits + string.punctuation
while not set(string.digits).intersection(set(password)) or \
not set(string.punctuation).intersection(set(password)):
    password = ''.join(random.choice(ch) for i in range(random.randint(8, 16)))

print(password)