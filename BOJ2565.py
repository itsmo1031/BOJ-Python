# 전깃줄 - 골드 5

N = int(input())
wire = []
for __ in range(N):
    wire.append(tuple(map(int, input().split())))

# 전깃줄을 A 전봇대 기준으로 정렬
wire.sort()
lis = [1] * N

for i in range(1, N):
    for j in range(0, i):
        # B 전봇대 기준으로 LIS 판별
        if wire[i][1] > wire[j][1]:
            lis[i] = max(lis[i], lis[j] + 1)

# 전체 전깃줄에서 LIS만큼을 빼면 없애야 하는 최소 전깃줄이 나옴
print(N - max(lis))
