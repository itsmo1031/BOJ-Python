# RGB거리 - 실버 1
# Dynamic Programming

N = int(input())
rgb = [[*map(int, input().split())] for __ in range(N)]

for i in range(1, N):
    for j in range(3):
        # 후보군 선정 (이전 색상을 제외한 나머지들)
        cand = rgb[i - 1].copy()
        cand.pop(j)
        # 둘중 최솟값을 현재 비용에 더해줌
        rgb[i][j] += min(cand)

print(min(rgb.pop()))
