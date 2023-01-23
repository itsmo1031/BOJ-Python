# 스티커 붙이기 - 골드 3
from functools import reduce

n, m, k = map(int, input().split())
laptop = [[0] * m for _ in range(n)]


def put(sticker: list) -> bool:
    y_offset = len(laptop[0]) - len(sticker[0]) + 1
    x_offset = len(laptop) - len(sticker) + 1
    if x_offset >= 1 and y_offset >= 1:
        for x in range(x_offset):
            for y in range(y_offset):
                # 스티커 붙이기
                for i in range(len(sticker)):
                    for j in range(len(sticker[0])):
                        laptop[x + i][y + j] += sticker[i][j]

                # 겹치는지 확인
                if check(laptop):
                    return True
                else:  # 겹치지 않으면 스티커 떼기
                    for i in range(len(sticker)):
                        for j in range(len(sticker[0])):
                            laptop[x + i][y + j] -= sticker[i][j]
    return False


def check(arr: list) -> bool:
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 1:
                return False
    return True


def rotate(arr: list) -> list:
    global rot_cnt
    rot_cnt += 1
    new_arr = [*map(list, zip(*arr[::-1]))]
    return new_arr


rot_cnt = 0

for _ in range(k):
    r, c = map(int, input().split())
    new_sticker = [[*map(int, input().split())] for _ in range(r)]

    while rot_cnt < 4:
        if put(new_sticker):
            break
        else:
            new_sticker = rotate(new_sticker)
    rot_cnt = 0

result = 0
for lap in laptop:
    result += reduce(lambda x, y: x + y, lap)
print(result)
