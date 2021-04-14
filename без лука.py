print('без лука')
mes = int(input())
n = []
for i in range(mes):
    m = input()
    if 'лук' not in m:
        n.append(m)
print(', '.join(n))