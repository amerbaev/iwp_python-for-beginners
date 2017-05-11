# a = int(input())
#
# n = []
#
# for i in range(1, a+1):
#     for j in range(i):
#         n.append(i)
#         if len(n) >= a:
#             break
#     if len(n) >= a:
#         break
#
# print(*n)

a = int(input())
print([i for j in range(i) for i in range(1, a)][:a])