string = input()

prev = None
count = 0
result = ''

for sym in string:
    if sym != prev and prev is not None:
        result += prev + str(count)
        count = 1
    else:
        count += 1
    prev = sym
result += prev + str(count)

print(result)