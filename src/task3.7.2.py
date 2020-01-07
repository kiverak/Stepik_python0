s1 = str(input())
s2 = str(input())
r1 = str(input())
r2 = str(input())
d = dict(zip(s1, s2))
s3, r3, = '', ''
for i in range(len(r1)):
    s3 += d[r1[i]]
print(s3)
for i in range(len(r2)):
    for key, value in d.items():
        if value == r2[i]:
            r3 += key
print(r3)