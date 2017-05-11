a = int(input())
b = int(input())

max_ab = max(a, b)
dividend = max_ab
divider = min(a, b)

while not dividend % divider == 0:
    dividend += max_ab

print(dividend)