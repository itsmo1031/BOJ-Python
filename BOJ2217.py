# 로프 - 실버 4

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort()
max_weight = 0
for i in range(1, n + 1):
    rope = ropes.pop()
    if max_weight <= rope * i:
        max_weight = rope * i

print(max_weight)
