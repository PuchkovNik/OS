print('Цезарь его знает')
n = int(input())
mes = input()
for k in mes:
    if not k.isalpha():
        print(k, end='')
        continue
    if ord(k) + n > 1071 and ord(k) <= 1071 or ord(k) + n > 1103 and ord(k) <= 1103:
        i = chr(ord(k) - 32)
    k = chr(ord(k) + n)
    print(k, end='')