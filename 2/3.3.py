a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('\t', '\t'.join([str(i) for i in range(c, d + 1)]))
for i in range(a, b + 1):
    elements = [str(i)]
    for j in range(c, d + 1):
        elements.append(str(i * j))
    print('\t'.join(elements))