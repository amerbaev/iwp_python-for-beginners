ticket_num = str(input())
print('Счастливый' if sum([int(ticket_num[i]) for i in range(3)]) == sum([int(ticket_num[i]) for i in range(3, 6)]) else 'Обычный')
