print('репосты')
lt = []
suma, name = 0, ''
for i in range(int(input())):
    m = input().split()
    suma += int(m[-1])
    lt.append(m)
lt[0][-1] = str(suma)
for j in range(len(lt)):
    n = lt[0][0]
    s = lt[j][0]
    for i in range(1, len(lt)):
        if s in lt[i] and n not in lt[i][4]:
            name = lt[i][4]
            cot = int(lt[i][-1])
            for l in range(len(lt)):
                if lt[l][0] in name:
                    lt[l][-1] = str(int(lt[l][-1]) + cot)
for v in lt:
    print(v[-1])