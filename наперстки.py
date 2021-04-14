print('Наперстки')
mes = int(input())
lt = [''] * mes
for i in range(mes):
    lt[i] = input()
k = int(input())
for i in range(k):
    m = int(input())
    tmp = [''] * m
    for j in range(m):
        tmp[j] = lt[int(input())-1]
    lt = tmp
for i in range(len(lt)):
    print(lt[i])