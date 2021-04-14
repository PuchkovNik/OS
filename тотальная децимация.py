print('тотальная децимация')
mes = int(input())
m = []
for i in range(mes):
    m.append(input())
k = int(input())
n = 0
print(m[0])
del m[0]
for i in range(mes):
    if len(m) > n + k - 1:
        n += k - 1
        print(m[n])
        del m[n]
    else:
        n = 0
        if len(m) > n:
            print(m[n])
            del m[n]