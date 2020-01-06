words = []
fr_words = []
d = dict()
max_counter = 0

with open('text.txt', 'r') as inf:
    words = inf.read().lower().split()

for i in range(len(words)):
    if words[i] in d:
        d[words[i]] += 1
    else:
        d[words[i]] = 1

for value in d.values():
    if value > max_counter:
        max_counter = value

for key, value in d.items():
    if value == max_counter:
        fr_words.append(key)
        # print(key, value)

fr_words.sort()
print(fr_words[0], max_counter)