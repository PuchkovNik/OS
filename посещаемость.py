print('Посещаемость')
n = int(input())
m = [set(input() for _ in range(int(input()))) for _ in range(n)]
res = m[0]
for i in m:
    res = res.intersection(i)
print(* sorted(res), sep = '\n')