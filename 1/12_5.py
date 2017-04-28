numbers = [int(input()) for i in range(3)]

print(max(numbers))
numbers.remove(max(numbers))
print(min(numbers))
numbers.remove(min(numbers))
print(numbers[0])