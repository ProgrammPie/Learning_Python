import random
import string

def password_generator(length: int, use_lower=True, use_upper=True,use_digits=True, use_symbols=False)->str:
    
    chars = ""

    if use_lower: chars += string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars +="!@#$%^&*"

    if not chars:
        return "No password!"

    return "".join(random.choices(chars,k=length))

print(f"Твой пароль:{password_generator(10,True,True,True,True):>15}.")