print('Фильтр')
from itertools import islice
import sys

mes = int(input('Введите кол-во строк: '))
for line in islice(sys.stdin, mes):
    if line.startswith("%%"):
        print(line[2:])
    elif not line.startswith('#' * 4):
        print(line)