# 덩치 - 실버 5
# Implementation

N = int(input())
data = []
for i in range(N):
    w, h = map(int, input().split())
    data.append((w, h))

result = [0] * N

for i in range(N):
    now = data[i]
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if data[j][0] > now[0] and data[j][1] > now[1]:
            rank += 1
        result[i] = rank

print(*result)
