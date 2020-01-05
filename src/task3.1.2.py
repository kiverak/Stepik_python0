lst = [1, 2, 3, 4, 5, 6]

def modify_list(l):
    for i in reversed(range(len(l))):
        if l[i] % 2 != 0:
            del l[i]
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = int(l[i] / 2)

print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]