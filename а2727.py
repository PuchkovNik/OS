print('а272727')
n = [0]
mes = int(input())
for i in range(mes):
    m = 0
    for f in range(len(n)):
        if n[f] == n[-1 - f]:
            m += 1
    n.append(m)
del n[-1]
for i in n:
    print(i)