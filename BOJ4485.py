# 녹색 옷 입은 애가 젤다지? - 골드 4
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline
num = 1

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)
        if cost > distance[x][y]:
            continue
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                nc = cost + graph[nx][ny]
                if nc < distance[nx][ny]:
                    distance[nx][ny] = nc
                    heapq.heappush(q, (nc, nx, ny))

    return distance[N - 1][N - 1]


while True:
    N = int(input())
    if N == 0:
        break

    graph = [[*map(int, input().split())] for __ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = graph[0][0]

    print(f"Problem {num}: {dijkstra()}")
    num += 1
