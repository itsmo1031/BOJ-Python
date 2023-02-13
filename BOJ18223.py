# 민준이와 마산 그리고 건우 - 골드 4
import heapq

INF = int(1e9)
V, E, P = map(int, input().split())

# 그래프 기본 정보 입력
graph: list[list[tuple]] = [[] for _ in range(V + 1)]
for __ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


# 다익스트라 알고리즘 정의
def dijkstra(sp):
    distance = [INF] * (V + 1)
    distance[sp] = 0

    q = []
    heapq.heappush(q, (0, sp))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for np, nd in graph[now]:
            cost = dist + nd
            if cost < distance[np]:
                distance[np] = cost
                heapq.heappush(q, (cost, np))

    return distance


from_start = dijkstra(1)
from_mj = dijkstra(P)

# 출발점에서 민준 + 민준에서 도착점까지의 거리가 출발점에서 도착점까지의 거리보다 작거나 같으면 구함
if from_start[V] >= from_start[P] + from_mj[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
