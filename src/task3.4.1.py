s, new_s = '', ''
i, cnt = 0, 0

with open('text.txt', 'r') as inf:
    s = inf.readline()

while i < len(s):
    if s[i].isalpha() or s[i] == '\n':
        if cnt > 0:
            num = ''
            for j in range(i - cnt, i):
                num += s[j]
            for j in range(int(num)):
                new_s += s[i - cnt - 1]
        if s[i] == '\n':
            new_s += s[i]
        i += 1
        cnt = 0
    elif s[i].isdigit():
        cnt += 1
        i += 1

with open('answer.txt', 'w') as ouf:
    ouf.write(new_s)