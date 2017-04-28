total_minutes = int(input())
bed_hours = int(input())
bed_minutes = int(input())

total_minutes += bed_hours * 60 + bed_minutes

alarm_hours = total_minutes // 60
alarm_minutes = total_minutes % 60

print(alarm_hours, alarm_minutes, sep='\n')