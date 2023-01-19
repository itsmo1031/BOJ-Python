import sys

n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [[*map(int, input().split())] for _ in range(n)]
clean = []
stack = 0

# 북 동 남 서 순
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def change_direction():
    global d
    d = (d - 1) % 4


while True:
    clean.append((x, y))

    while True:
        if stack == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            if room[nx][ny] == 1:
                print(len(clean))
                sys.exit()
            else:
                x = nx
                y = ny
                stack = 0
                continue

        change_direction()
        nx = x + dx[d]
        ny = y + dy[d]
        if room[nx][ny] == 0 and (nx, ny) not in clean:
            x = nx
            y = ny
            stack = 0
            break
        if room[nx][ny] == 1 or (nx, ny) in clean:
            stack += 1
            continue
