print('Новые блюда')
k = set()
m = set()
i = int(input())
for i in range(i):
    k.add(input())
i = 0
i = int(input())
for i in range(i):
    d = int(input())
    for a in range(d):
        m.add(input())
q = list(k - m)
v = sorted(q)
print(*v, sep='\n')