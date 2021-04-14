print('Белый список')
white = []
for i in range(int(input())):
    white.append(input())
search = []
for j in range(int(input())):
    search.append(input())
for n in search:
    if n in white:
        print(n)
