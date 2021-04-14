print('два пути')
mes = int(input())
ft = [int(input()) for i in range(mes)]
sd = ft[:]
tran = int(input())
for i in range(tran):
    brother = int(input())
    if brother == 1:
        ft[int(input())] += int(input())
    elif brother == 2:
        sd[int(input())] += int(input())
print(*ft)
print(*sd)