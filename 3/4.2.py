with open('dataset_3363_2.txt') as data:
    in_str = data.read()

i = 0
sym = ''
mult = ''
for i in in_str:
    if i in '1234567890':
        mult += i
    else:
        if mult:
            print(sym * int(mult), end='')
        mult = ''
        sym = i
