# 지름길 - 실버 1
import heapq

INF = int(1e9)
N, D = map(int, input().split())
graph = [[] for __ in range(D + 1)]
distance = [INF] * (D + 1)

"""
지름길이 아닌 일반 도로의 정보를 입력해줘야 함
간단하게 생각해서 인접한 노드 사이의 거리를 1로 설정하면 됨.
"""
for i in range(D):
    graph[i].append((i + 1, 1))

for __ in range(N):
    s, e, v = map(int, input().split())
    if e > D:
        continue
    graph[s].append((e, v))

q = []
heapq.heappush(q, (0, 0))
distance[0] = 0

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for np, nd in graph[now]:
        cost = dist + nd
        if cost < distance[np]:
            distance[np] = cost
            heapq.heappush(q, (cost, np))

print(distance[D])
