s = [int(i) for i in input().split()]
s.sort()
cnt, i = 0, 1
cnt2 = 0
while i < len(s):
    if cnt == 0 and s[i] == s[i - 1]:
        if cnt2 == 0:
            print(s[i], end='')
        elif cnt2 > 0:
            print('', s[i], end='')
        cnt += 1
        cnt2 = 1
    elif cnt > 0 and s[i] != s[i - 1]:
        cnt = 0
    i += 1
