print('16.2 CSV')
sp = []
for _ in range(int(input())):
    mes = input().split(',')
    sp.append(mes)
for _ in range(int(input())):
    position = input().split(',')
    x, y = int(position[0]), int(position[1])
    print(sp[x][y])