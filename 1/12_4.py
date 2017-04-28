from math import sqrt

form = input()

if form == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())

    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
elif form == 'прямоугольник':
    a = int(input())
    b = int(input())

    s = a * b
elif form == 'круг':
    r = int(input())

    s = 3.14 * r**2

print(s)