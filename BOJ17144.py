# 미세먼지 안녕! - 골드 4
# 구현 문제
import copy
import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())
room: list[list[int]] = []
purifier = []
for i in range(r):
    row = [*map(int, input().split())]
    for j in range(c):
        if row[j] == -1:
            purifier.append((i, j))
    room.append(row)

# 상-우-하-좌
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def spread():
    global room
    dust = [[0] * c for __ in range(r)]
    for x in range(r):
        for y in range(c):
            if room[x][y] != 0 and room[x][y] != -1:
                cnt = 0
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        dust[nx][ny] += room[x][y] // 5
                        cnt += 1
                if cnt > 0:
                    dust[x][y] += room[x][y] - (room[x][y] // 5) * cnt
    for px, py in purifier:
        dust[px][py] = -1
    room = copy.deepcopy(dust)


def purify():
    cd = 0
    # 위-아래 순으로 공청기 동작
    for k in range(2):
        if k == 1:
            cd = 2
        px, py = purifier[k]
        x = px
        y = py
        while True:
            nx = x + d[cd][0]
            ny = y + d[cd][1]

            # 공청기의 회전 범위 설정
            if k == 0:
                if nx < 0 or nx > px or ny < 0 or ny >= c:
                    cd = (cd + 1) % 4
                    continue
            else:
                if nx < px or nx >= r or ny < 0 or ny >= c:
                    cd = (cd - 1) % 4
                    continue

            if nx == purifier[k][0] and ny == purifier[k][1]:
                break

            if room[x][y] != -1:
                room[x][y] = room[nx][ny]

            room[nx][ny] = 0
            x = nx
            y = ny


for __ in range(t):
    spread()
    purify()

result = 2
for row in room:
    result += sum(row)

print(result)
