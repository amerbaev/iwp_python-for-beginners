n = int(input())

calculated = {}

for _ in range(n):
    key = int(input())
    if key not in calculated:
        calculated[key] = f(key)

    print(calculated[key])
