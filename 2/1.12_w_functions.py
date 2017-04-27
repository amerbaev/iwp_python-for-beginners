def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a*b//gcd(a, b))