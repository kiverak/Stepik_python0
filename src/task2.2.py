i = 0
while i <= 100:
    i = int(input())
    if i < 10:
        continue
    elif i > 100:
        break
    else:
        print(i)
