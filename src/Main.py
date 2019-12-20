a, b, c = int(input()), int(input()), int(input())

maximum = max(a, b, c)
minimum = min(a, b, c)

if (minimum == a and maximum == b) or (maximum == a and minimum == b):
    mid = c
elif (minimum == c and maximum == b) or (maximum == c and minimum == b):
    mid = a
elif (minimum == a and maximum == c) or (maximum == a and minimum == c):
    mid = b
else:
    mid = minimum

print(maximum)
print(minimum)
print(mid)