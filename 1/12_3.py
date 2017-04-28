num_1 = float(input())
num_2 = float(input())
action = input()

if action in ('/', 'mod', 'div') and num_2 == 0:
    print('Деление на 0!')
else:
    if action == '+':
        print(num_1 + num_2)
    elif action == '-':
        print(num_1 - num_2)
    elif action == '*':
        print(num_1 * num_2)
    elif action == '/':
        print(num_1 / num_2)
    elif action == 'mod':
        print(num_1 % num_2)
    elif action == 'pow':
        print(num_1 ** num_2)
    elif action == 'div':
        print(num_1 // num_2)