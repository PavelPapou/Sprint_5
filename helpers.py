import random
import string

def generate_email():
    random_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    random_url = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f'{random_name}@{random_url}.com'

def generate_password():
    return (random.choices(string.digits, k=8))