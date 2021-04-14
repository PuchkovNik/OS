print('гэдсби')
a = input()
print(*[i for i in input().split() if a.upper() in i or a in i], sep='\n')
