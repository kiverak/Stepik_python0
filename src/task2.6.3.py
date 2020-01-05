lst = [int(i) for i in input().split()]
x = int(input())
cnt = False
for i in range(len(lst)):
    if x == lst[i]:
        print(i, end=" ")
        cnt = True
if cnt == False:
    print("Отсутствует")