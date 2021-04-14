print('Сор-ка в обр-ом порядке')
def asort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i):
            j1 = j + i
            if a[j1] > a[i]:
                tmp = a[i]
                a[i] = a[j1]
                a[j1] = tmp
n = int(input())
arr = []
for i in range(n):
    arr += [int(input())]
asort(arr)
for i in arr:
    print(i)