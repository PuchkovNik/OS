print('пристраиваемся в очередь')
mes = int(input())
m = []
for _ in range(mes):
    n = input().split()
    if 'встал' in n[1]:
        m.append(n[0])
    elif n[0] == 'Привет,':
        m.insert(m.index(n[1][:-1])+1, n[2])
    elif n[1] == 'хватит':
        m.remove(n[0][:-1])
print(*m, sep='\n')