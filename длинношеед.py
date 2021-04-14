print('длинношеед')
mes = input()
mes = mes.upper()
m = 0
for i in range(0, len(mes)):
    if mes.count(mes[i]) > m:
        m = mes.count(mes[i])
print(m)