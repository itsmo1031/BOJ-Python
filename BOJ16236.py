# 아기 상어 - 골드 3
from collections import deque

N = int(input())
sea = []
shark = []
for i in range(N):
    sea.append([*map(int, input().split())])
    for j in range(N):
        if sea[i][j] == 9:
            sea[i][j] = 0
            shark = [(i, j), 2]


def edible_f(size):
    arr = []
    for i in range(N):
        for j in range(N):
            if 0 < sea[i][j] < size:
                arr.append((i, j))
    arr.sort()
    return arr


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def shortest(arr):
    tmp = []
    for fx, fy in arr:
        visited = [[False] * N for _ in range(N)]
        q = deque([[shark[0], 0]])
        while q:
            qp, s_len = q.popleft()
            qx, qy = qp
            if (qx, qy) == (fx, fy):
                tmp.append([(fx, fy), s_len])
                break
            for dx, dy in d:
                nx = qx + dx
                ny = qy + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if sea[nx][ny] > shark[1]:
                        continue
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([(nx, ny), s_len + 1])
    return min(tmp, key=lambda x: x[1]) if tmp else []


answer = 0
e_cnt = 0
while True:
    fish = edible_f(shark[1])
    if not fish:
        break
    else:
        possible = shortest(fish)
    if not possible:
        break
    p, length = possible
    x, y = p
    sx, sy = shark[0]
    answer += length
    sea[x][y] = 0
    shark[0] = (x, y)
    e_cnt += 1
    if e_cnt == shark[1]:
        shark[1] += 1
        e_cnt = 0

print(answer)
