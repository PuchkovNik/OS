print('Розенкранц')
m = input()
dl = len(m)
k = 0
max_len = 0
for i in range(dl):
    if 'о' in m:
        k += 1
        max_len = k
        if 'р' in m[i]:
            k = 0
            continue
    if k > max_len:
        max_len = k
print(max_len - 1)