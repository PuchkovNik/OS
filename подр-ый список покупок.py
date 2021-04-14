print('Подробный список покупок')
a = []
b = []
for i in range(int(input())):
    a.append(input())
    b.append(int(input()))
for i in range(len(b)):
    print(a[len(a) - 1 - i], b[len(b) - 1 - i])
