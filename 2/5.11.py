numbers = sorted([int(i) for i in input().split(' ')])

doubles = []
i = 0

while i < len(numbers) - 1:
    if numbers[i] == numbers[i + 1]:
        if numbers[i] not in doubles:
            doubles.append(numbers[i])
        numbers.pop(i + 1)
    else:
        i += 1

print(' '.join([str(i) for i in doubles]))