total_minutes = int(input())

alarm_hours = total_minutes // 60
alarm_minutes = total_minutes % 60

print(alarm_hours, alarm_minutes, sep='\n')

