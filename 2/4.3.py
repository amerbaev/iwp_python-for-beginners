string = input().lower()

result = ( string.count('g') + string.count('c') ) * 100 / len(string)

print(result)