print('Именно та буква')
s = input().lower()
n = int(input())-1
l = input().lower()
if (0<n<=len(s)) and (l in s) and (len(l)==1):
    print('ДА') if s[n]==l else print('НЕТ')
else:
    print('ОШИБКА')