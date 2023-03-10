# 영단어 암기는 괴로워 - 실버 3

N, M = map(int, input().split())

data = dict()

for __ in range(N):
    word = input()
    if len(word) >= M:
        if word in data:
            data[word] += 1
        else:
            data[word] = 1

result = sorted(data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for r in result:
    print(r[0])
