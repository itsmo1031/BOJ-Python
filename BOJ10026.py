# 적록색약 - 골드 5
from collections import deque

N = int(input())
p = [[*input()] for __ in range(N)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def see(paint, blind):
    index = 1
    section = [[0] * N for __ in range(N)]
    for i in range(N):
        for j in range(N):
            if section[i][j] == 0:
                q = deque([(i, j)])
                color = paint[i][j]
                if blind and (color == 'G' or color == 'R'):
                    color = 'GR'
                section[i][j] = index
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < N and not section[nx][ny]:
                            if paint[nx][ny] in color:
                                section[nx][ny] = index
                                q.append((nx, ny))
                index += 1
    return index - 1


print(see(p, False), see(p, True))
