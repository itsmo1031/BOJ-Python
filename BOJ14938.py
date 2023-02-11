# 서강그라운드 - 골드 4

INF = int(1e9)
n, m, r = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
item = [*map(int, input().split())]

for __ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(n + 1):
    graph[i][i] = 0

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = 0
for g in graph:
    total = 0
    for gi in range(1, n + 1):
        if g[gi] <= m:
            total += item[gi - 1]
    res = max(res, total)

print(res)
