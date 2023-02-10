# 택배 배송 - 골드 5
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
distance = [INF] * (N + 1)
graph = [[] for __ in range(N + 1)]

for __ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for np, nd in graph[now]:
        cost = dist + nd
        if cost < distance[np]:
            distance[np] = cost
            heapq.heappush(q, (cost, np))

print(distance[N])
