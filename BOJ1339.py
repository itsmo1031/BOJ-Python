# 단어 수학 - 골드 4

n = int(input())
words = []
reverse = []
for _ in range(n):
    words.append(input())
for word in words:
    reverse.append([*word[::-1]])

d = {}
for r in reverse:
    for k in range(len(r)):
        d[r[k]] = d.get(r[k], 0) + 10 ** k

seq = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
idx = [str(x) for x in range(9, 9 - len(seq), -1)]
result = 0
for word in words:
    result += int(word.translate(word.maketrans(''.join(seq.keys()), ''.join(idx))))

print(result)
