# 인간 대포 - 골드 2
# 다익스트라 알고리즘
import heapq

INF = 1e9


# 거리 계산 함수 정의
def calc(sp, ep):
    sx, sy = sp
    ex, ey = ep
    return ((sx - ex) ** 2 + (sy - ey) ** 2) ** 0.5


# 다익스트라 알고리즘 정의
def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        dist, p = heapq.heappop(q)
        if dist > distance[p]:
            continue
        for np, nd in graph[p]:
            cost = nd + dist
            if cost < distance[np]:
                distance[np] = cost
                heapq.heappush(q, (cost, np))


start = tuple(map(float, input().split()))
end = tuple(map(float, input().split()))
n = int(input())
distance = [INF] * (n + 2)
graph = [[] for __ in range(n + 2)]
pos = [start]  # 시작/끝점과 각 대포의 좌표를 담을 리스트
distance[0] = 0

# 리스트에 각 좌표 담기
for __ in range(n):
    pos.append(tuple(map(float, input().split())))
pos.append(end)

# 출발점부터 각 대포까지의 거리를 계산하여 집어넣음
for i in range(0, n + 2):
    now = pos[i]
    for j in range(0, n + 2):
        if i != j:
            new = pos[j]
            walk = calc(now, new) / 5
            if i == 0:
                graph[i].append((j, walk))
            else:
                graph[i].append((j, min(walk, 2 + abs(calc(now, new) - 50) / 5)))

dijkstra()

print(distance[n + 1])
