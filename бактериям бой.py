mes = int(input())
lt = []
for i in range(mes):
    lt.append([0] * mes)
for j in range(mes):
    for b in range(mes):
        lt[j][b] = int(input())
k = int(input())
for c in range(k):
    y, x = int(input()), int(input())
    lt[x][y] -= 8
    if x - 1 >= 0 and y - 1 >= 0:
        lt[x - 1][y - 1] -= 4
    if x - 1 >= 0:
        lt[x - 1][y] -= 4
    if y - 1 >= 0:
        lt[x][y - 1] -= 4
    if x + 1 < mes and y + 1 < mes:
        lt[x + 1][y + 1] -= 4
    if x + 1 < mes:
        lt[x + 1][y] -= 4
    if y + 1 < mes:
        lt[x][y + 1] -= 4
    if x - 1 >= 0 and y + 1 < mes:
        lt[x - 1][y + 1] -= 4
    if x + 1 < mes and y - 1 >= 0:
        lt[x + 1][y - 1] -= 4
for f in range(mes):
    for d in range(mes):
        if lt[f][d] < 0:
            lt[f][d] = 0
for i in range(mes):
    lt[i] = ' '.join(str(v) for v in lt[i])
print('\n'.join(lt))