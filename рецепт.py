print('Новые блюда')
N = False
IHM = set()
IE = set()
IH = int(input())
for i in range(IH):
    IHM.add(input())
NR1 = int(input())
for i in range(NR1):
    NR = input()
    IE1 = int(input())
    for j in range(IE1):
        IE.add(input())
    for i in IE:
        if i in IHM:
            N = True
        else:
            N = not True
    if N:
        print(NR)
    IE = set()