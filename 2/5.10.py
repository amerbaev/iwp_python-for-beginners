numbers = [int(i) for i in input().split(' ')]

if len(numbers) >= 3:
    sums = [numbers[i - 1] + numbers[i + 1 - len(numbers)] for i in range(len(numbers))]
    # sums.append(numbers[0] + numbers[-2])
else:
    sums = numbers

print(' '.join([str(i) for i in sums]))