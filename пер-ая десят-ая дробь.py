print('Пер-ая десят-ая дробь')
mes = int(input())
n = 1
ar = []
ad = []
while n not in ar:
    ar.append(n)
    ad.append(10 * n // mes)
    n = 10 * n % mes
print(*ad[ar.index(n):])
