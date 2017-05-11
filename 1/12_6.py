number = int(input())

number_mod_10 = number % 10
number_mod_100 = number % 100
default_str = 'программист'

if 10 < number_mod_100 < 20:
    print(number, default_str + 'ов ')
else:
    if number_mod_10 == 1:
        print(number, default_str + ' ')
    elif number_mod_10 == 0 or number_mod_10 in range(5, 10):
        print(number, default_str + 'ов ')
    elif number_mod_10 in range(2, 5):
        print(number, default_str + 'a ')