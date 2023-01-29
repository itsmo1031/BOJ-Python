# 토마토 - 골드 4

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
t_box = []
for __ in range(H):
    t_box.append([[*map(int, input().split())] for _ in range(N)])

d = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

visited = [[[False] * M for _ in range(N)] for _ in range(H)]


def get_tmt_info():
    tmt = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if t_box[i][j][k] == 1:
                    tmt.append([(i, j, k), 0])
                    visited[i][j][k] = True
    return tmt


def check():
    for t in t_box:
        for r in t:
            if 0 in r:
                return True
    return False


def mature():
    days = 0
    q = deque(get_tmt_info())
    while q:
        tmt_info, days = q.popleft()
        z, x, y = tmt_info
        for dz, dx, dy in d:
            nz = z + dz
            nx = x + dx
            ny = y + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and not visited[nz][nx][ny]:
                if t_box[nz][nx][ny] == 0:
                    t_box[nz][nx][ny] = 1
                    visited[nz][nx][ny] = True
                    q.append([(nz, nx, ny), days + 1])
    return -1 if check() else days


print(mature())
