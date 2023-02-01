# Two Dots - 골드 4

N, M = map(int, input().split())
board = [[*input()] for _ in range(N)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cycle = False


def dfs(pos, visited):
    global cycle
    if cycle:
        return
    visited.append(pos)
    x, y = pos
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == board[x][y]:
                if len(visited) >= 4 and (nx, ny) == visited[0]:
                    cycle = True
                else:
                    if (nx, ny) not in visited:
                        dfs((nx, ny), visited.copy())


for i in range(N):
    for j in range(M):
        if not cycle:
            dfs((i, j), [])

print("Yes") if cycle else print("No")
