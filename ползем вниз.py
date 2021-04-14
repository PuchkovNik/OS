print('Ползем вниз')
stroka = input()
ch_r = stroka[0]
print(ch_r, end='')
n = 0
k = 0
m = 0
for i in range(1, len(stroka)):
    if stroka[i] == '>':
        print(ch_r, end='')
        n += 1
    elif stroka[i] == 'V':
        print()
        print((n - m) * ' ' + ch_r, end='')
        k += 1
    elif stroka[i] == '<':
        print((n - k - m) * ' ' + ch_r, end='')
        m += 1