# 파티 - 골드 3
# 다익스트라 알고리즘 사용
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for np, nd in graph[now]:
            cost = dist + nd
            if cost < distance[np]:
                distance[np] = cost
                heapq.heappush(q, (cost, np))
    return distance[end]


N, M, X = map(int, input().split())
graph = [[] for __ in range(N + 1)]

for __ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = [dijkstra(i, X) + dijkstra(X, i) for i in range(1, N + 1)]

print(max(result))
