n = int(input())
words = set()
for i in range(n):
    s = str(input()).lower().split()
    for j in range(len(s)):
        words.add(s[j])
m = int(input())
text = []
for i in range(m):
    s = str(input()).lower().split()
    for j in range(len(s)):
        text.append(s[j])
errors = set()
for i in range(len(text)):
    if text[i] not in words:
        errors.add(text[i])
for err in errors:
    print(err)