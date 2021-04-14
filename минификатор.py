print('Минификатор')
n = int(input())

otm = False
sl = False

char = 0
res = []

for i in range(n):
    string = input()
    while string[char] == " ":
        res.append(" ")
        char += 1
    for i2 in range(char, len(string)):
        if not sl:
            if string[i2] == "'":
                res.append(string[i2])
                otm = not otm
            elif string[i2] == "\\":
                res.append(string[i2])
                sl = True
            elif string[i2] == "#":
                if otm:
                    res.append(string[i2])
                else:
                    break
            elif string[i2] == " ":
                if otm:
                    res.append(string[i2])
                else:
                    if i2 + 1 != len(string):
                        if string[i2 + 1] == " ":
                            res.append("")
                        else:
                            res.append(string[i2])
            else:
                res.append(string[i2])
        else:
            sl = False
            res.append(string[i2])
    print("".join(res))
    res = []
    otm = False
    sl = False
    char = 0