tabel = dict()
cnt = 0
sum0, sum1, sum2 = 0, 0, 0

with open('text.txt', 'r') as inf:
    while True:
        string = inf.readline()
        if len(string) == 0:
            break
        if string[len(string) - 1] == '\n':
            string = string[:len(string)-1]
        student = string.split(';')
        tabel[student[0]] = [int(student[1]), int(student[2]), int(student[3])]

for key, value in tabel.items():
    print((value[0] + value[1] + value[2]) / 3)
    cnt += 1
    sum0 += value[0]
    sum1 += value[1]
    sum2 += value[2]

print(sum0/cnt, sum1/cnt, sum2/cnt)