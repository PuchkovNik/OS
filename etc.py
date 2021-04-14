print('etc')
a = []
b = []
c = []
d = []
while True:
    d.clear()
    e = input()
    if e == '':
        break
    else:
        d = e.split(':')
        f = d[4].split(',')
        b.append(d[0])
        a.append(f[0])
        c.append(d[1])
g = input().split(';')
for i in range(len(c)):
    if c[i] in g:
        print('To:', b[i])
    print(a[i], ', ваш пароль слишком простой, смените его.', sep='')
