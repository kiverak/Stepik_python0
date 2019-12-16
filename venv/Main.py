X = int(input())
H = int(input())
M = int(input())

X = X + H * 60 + M
hours = X // 60
minutes = X - hours * 60;

print(hours)
print(minutes)