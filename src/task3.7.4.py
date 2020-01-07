n = int(input())
dir = {'север':[0, 1], 'восток':[1, 0], 'юг':[0, -1], 'запад':[-1, 0]}
coords = [int(0), int(0)]
for i in range(n):
    s = str(input()).split()
    coords[0] += dir[s[0]][0] * int(s[1])
    coords[1] += dir[s[0]][1] * int(s[1])
print(coords[0], coords[1])