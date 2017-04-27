a = int(input())
b = int(input())

wo_mod = False
max_ab = max(a, b)
dividend = max_ab
divider = min(a, b)
while not wo_mod:
    if dividend % divider == 0:
        wo_mod = True
    else:
        dividend += max_ab

print(dividend)