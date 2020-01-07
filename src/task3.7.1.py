n = int(input())
championship = dict()   # {team: [wins, looses, draws]}
for i in range(n):
    game = str(input()).split(';')
    if game[1] > game[3]:
        if game[0] not in championship:
            championship[game[0]] = [int(1), int(0), int(0)]
        else:
            championship[game[0]][0] += 1
        if game[2] not in championship:
            championship[game[2]] = [int(0), int(1), int(0)]
        else:
            championship[game[2]][1] += 1
    if game[1] < game[3]:
        if game[0] not in championship:
            championship[game[0]] = [int(0), int(1), int(0)]
        else:
            championship[game[0]][1] += 1
        if game[2] not in championship:
            championship[game[2]] = [int(1), int(0), int(0)]
        else:
            championship[game[2]][0] += 1
    if game[1] == game[3]:
        if game[0] not in championship:
            championship[game[0]] = [int(0), int(0), int(1)]
        else:
            championship[game[0]][2] += 1
        if game[2] not in championship:
            championship[game[2]] = [int(0), int(0), int(1)]
        else:
            championship[game[2]][2] += 1
# print(championship)
for key, value in championship.items():
    print(key, end='')
    print(':', end='')
    score = value[0] * 3 + value[2]
    print(value[0] + value[1] + value[2], value[0], value[2], value[1], score)