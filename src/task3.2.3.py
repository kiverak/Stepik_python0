def f(x):
    return x**2

n = int(input())
d = dict()
for i in range(n):
    x = int(input())
    if x not in d:
        d[x] = f(x)
    print(d[x])