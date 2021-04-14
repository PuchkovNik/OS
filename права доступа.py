print('права доступа')
lt = {}
for i in range(int(input())):
    m = input()
    lt[m] = lt.get(m)
for j in range(int(input())):
    new = ''
    k = False
    for i in input().split('/'):
        if i:
            new = new + '/' + i
        if new in lt:
            k = True
    if k:
        print('YES')
    else:
        print('NO')