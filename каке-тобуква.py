print('Какае-то буква')
sl = input()
sim = int(input())
if sim > len(sl) or sim < 1:
    print('ОШИБКА')
else:
    print(sl[sim - 1])