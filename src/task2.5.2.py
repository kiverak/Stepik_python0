s = input().split()
i = 0
for j in range (len(s)):
    s[j] = int(s[j])
s1 = [0] * len(s)
if len(s) == 1:
    s1[0] = s[0]
else:
    while i < len(s):
        if i == 0:
            s1[i] = s[len(s) - 1] + s[1]
        elif i == len(s) - 1:
            s1[i] = s[i - 1] + s[0]
        else:
            s1[i] = s[i - 1] + s[i + 1]
        i += 1
for j in range(len(s1)):
    print(s1[j], end=' ')
