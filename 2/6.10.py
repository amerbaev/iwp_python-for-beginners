matr = []

while True:
    a = input()
    if a == 'end':
        break

    a = a.split()
    a = [int(i) for i in a]
    matr.append(a)

stlb = len(matr)
strk = len(matr[0])
result = []
for i in range(stlb):
    new_str = []
    for j in range(strk):
        new_str.append(matr[i - 1][j] + \
                       matr[i + 1 - stlb][j] + \
                       matr[i][j - 1] + \
                       matr[i][j + 1 - strk])
    result.append(new_str)

for i in result:
    print(*i)
