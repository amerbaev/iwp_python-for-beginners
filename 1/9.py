total_minutes = int(input())
dream_hours = int(input())
dream_minutes = int(input())

dream_total = dream_hours * 60 + dream_minutes

total_minutes += dream_total

hours = total_minutes // 60
exc_minutes = total_minutes % 60

print(hours)
print(exc_minutes)