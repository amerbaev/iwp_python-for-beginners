total = 0
numbers = []

while True:
    numbers.append(int(input()))
    if sum(numbers) == 0:
        break

print(sum([i**2 for i in numbers]))

