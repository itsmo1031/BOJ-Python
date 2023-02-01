# 숫자판 점프 - 실버 2

board = [[*input().split()] for __ in range(5)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y, num):
    if len(num) == 6:
        return answer.add(num)

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            new_num = num + board[nx][ny]
            dfs(nx, ny, new_num)


answer = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(answer))
