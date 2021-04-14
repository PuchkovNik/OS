print('Однофамильцы')
m = int(input())
MW = [input() for _ in range(m)]
res = 0
for var in set(MW):
    count = 0
    for name in MW:
        if var == name:
            count += 1
    if count > 1:
        res += count
print(res)