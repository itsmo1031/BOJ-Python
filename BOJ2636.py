# TODO: bfs function 한 번만 사용해서 다시 풀기

from collections import deque

r, c = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(r)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def make_air(pos):
    air = [pos]
    q = deque([pos])
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c and not check[nx][ny]:
                if board[nx][ny] != 1:
                    q.append((nx, ny))
                    check[nx][ny] = True
                if board[nx][ny] == 0:
                    air.append((nx, ny))
    for x, y in air:
        board[x][y] = 2


def bfs(pos):
    q = deque([pos])
    cheese = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cheese += 1
                if board[nx][ny] == 2:
                    board[x][y] = 2
    return cheese


def check_cheese(graph):
    for g in graph:
        if 1 in g:
            return True
    return False


time = 0

while True:
    visited = [[False] * c for _ in range(r)]
    check = [[False] * c for _ in range(r)]
    cnt = 0
    make_air((0, 0))

    for i in range(r):
        for j in range(c):
            if board[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                cnt += bfs((i, j))
    time += 1

    if not check_cheese(board):
        break

print(time)
print(cnt)
