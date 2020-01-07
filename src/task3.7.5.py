with open('text.txt', 'r') as inf:
    s = inf.readline().split()
    school_table = [[int(s[0]), s[1], int(s[2])]]
    while True:
        s = inf.readline().split()
        if len(s) <= 1:
            break
        school_table.append([int(s[0]), s[1], int(s[2])])
for i in range(1, 12):
    sum, cnt = 0, 0
    for j in range(len(school_table)):
        if school_table[j][0] == i:
            sum += school_table[j][2]
            cnt += 1
    if cnt != 0:
        print(i, sum / cnt)
    else:
        print(i, '-')