# 2xn 타일링 2 - 실버 3

n = int(input())

tile = [0] * 1000
tile[0] = 1
tile[1] = 3

for i in range(2, 1000):
    tile[i] = (tile[i - 1] + tile[i - 2] * 2) % 10007

print(tile[n - 1])
