# RGB거리 2 - 실버 4
# Dynamic Programming
import copy

N = int(input())
rgb = [[*map(int, input().split())] for __ in range(N)]

INF = int(1e9)
result = INF

# 첫 번째 색상(k)을 고정해두고 체크
for k in range(3):
    tmp = copy.deepcopy(rgb)

    # 정해진 색상 외의 나머지 색상은 무한대로 초기화(최소값을 얻도록)
    for m in range(3):
        if m != k:
            tmp[0][m] = INF

    for i in range(1, N):
        for j in range(3):
            cand = tmp[i - 1].copy()
            cand.pop(j)
            tmp[i][j] += min(cand)

    res = tmp.pop()
    res.pop(k)  # N번 집의 색은 1번 집의 색과 같지 않아야 함.

    result = min(result, min(res))

print(result)
