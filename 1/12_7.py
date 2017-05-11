ticket_num = str(input())
# print('Счастливый'
#       if sum([int(ticket_num[i]) for i in range(3)]) == sum([int(ticket_num[i]) for i in range(3, 6)])
#       else 'Обычный')

sum_0 = sum( [int(i) for i in ticket_num[0:3]] )
sum_1 = sum( [int(i) for i in ticket_num[3:6]] )

print('Счастливый' if sum_0 == sum_1 else 'Обычный')


