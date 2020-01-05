n = int(input())
a = [[0] * n for el in range(n)]

i, j, d = 0, 0, 0
moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
for k in range(1, n * n + 1):
    a[i][j] = k
    for l in range(4):
        newD = (d + l) % 4
        di, dj = moves[newD]
        newI, newJ = i + di, j + dj
        if 0 <= newI < n and 0 <= newJ < n and a[newI][newJ] == 0:
            i, j, d = newI, newJ, newD
            break

for el in a:
    print(*el)