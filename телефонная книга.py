lt = {}
for i in range(int(input())):
    value, key = input().split()
    if key in lt:
        lt[key].append(value)
    else:
        lt[key] = [value]
for j in range(int(input())):
    key = input()
    print(*lt.get(key, ['Нет в телефонной книге']))