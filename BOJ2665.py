# 미로만들기 - 골드 4
# 다익스트라 알고리즘을 사용하여 반전된 그래프의 n,n위치까지의 거리값을 리턴
import heapq

INF = int(1e9)
n = int(input())
# 입력된 그래프를 반전(검은 방이 1이고 흰 방이 0이 되게끔)시켜 x,y까지의 거리값을 담은 그래프로 변환
graph = [[*map(lambda x: (int(x) + 1) % 2, input())] for __ in range(n)]
# 최단 거리 테이블 초기화
distance = [[INF] * n for __ in range(n)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dijkstra():
    q = []
    # cost, x, y좌표
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))


dijkstra()

print(distance[n - 1][n - 1])
