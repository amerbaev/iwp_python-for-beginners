at_least = int(input())
no_more = int(input())
current = int(input())

if current < at_least:
    print('Недосып')
elif current > no_more:
    print('Пересып')
else:
    print('Это нормально')