n = int(input())
i = 0
cnt = 1
while i < n:
    j = 0
    while j < cnt and i < n:
        print(cnt, end=" ")
        j += 1
        i += 1
    cnt += 1