# 회장뽑기 - 골드 5
# 플로이드 워셜 알고리즘

INF = int(1e9)
n = int(input())
graph = [[INF] * n for __ in range(n)]

for i in range(n):
    graph[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = [*map(max, graph)]
cand = min(result)

print(cand, result.count(cand))
for i in range(n):
    if result[i] == cand:
        print(i + 1, end=" ")
