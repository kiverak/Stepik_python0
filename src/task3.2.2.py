a = input().split()
d = dict()

for i in range(len(a)):
    a[i] = a[i].lower()
    if a[i] in d:
        d[a[i]] = d[a[i]] + 1
    else:
        d[a[i]] = 1

for key, value in d.items():
    print(key, value)