from charc import *
from random import choices, shuffle

pwd_length = int(input('Enter the length of the password: '))

special = int(input(f'Enter the num of special character: '))
number = int(input(f'Enter the num of number character: '))
low_charc = int(input('Enter the num of lower character: '))
up_charc = int(input('Enter the num of upper charcter: '))

if (special + number + low_charc + up_charc) == pwd_length:
    s = choices(symbols,  k=special)
    n = choices(digits,  k=number)
    l = choices(lower_char,  k=low_charc)
    u = choices(upper_char,  k=up_charc)

    # shuffle
    shuffle_pwd = s + n + l + u
    shuffle(shuffle_pwd)

    password = ''.join(shuffle_pwd)
    print(password)
else:
    print('Error')

