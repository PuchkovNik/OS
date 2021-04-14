print('знаков без пробелов')
mes = input()
m = 0
for a in mes:
    if a != ' ' and a != '\t':
        m += 1
print(m)