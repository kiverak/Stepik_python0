s = str(input())
new_s = ""
i = 0
cnt = 0
while i < len(s):
    if cnt == 0:
        new_s = new_s + s[i]
        cnt += 1
    else:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            new_s += str(cnt)
            new_s += s[i]
            cnt = 1
    if i + 1 == len(s):
        new_s += str(cnt)
    i += 1

print(new_s)
