inp = ''
a = []
b = []
while inp != 'end':
    inp = input()
    if inp != "end":
        inp = inp.split()
    a.append(inp)
del a[len(a) - 1]

if len(a) != 0:
    n, m = len(a), len(a[0])
    for i in range(n):
        string = []
        for j in range(m):
            sum = int(a[i][j - 1]) + int(a[i][j + 1 - m]) + int(a[i - 1][j]) + int(a[i + 1 - n][j])
            string.append(sum)
        b.append(string)

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=" ")
    print()
