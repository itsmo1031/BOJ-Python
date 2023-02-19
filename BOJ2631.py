# 줄세우기 - 골드 4
# LIS 찾은 후 전체에서 빼주면 옮겨야 하는 최소 횟수가 나옴.

N = int(input())

child = [int(input()) for __ in range(N)]

lis = [1] * N

# 가장 긴 증가하는 부분 수열(LIS) 찾기
for i in range(1, N):
    for j in range(i):
        if child[i] > child[j]:
            lis[i] = max(lis[i], lis[j] + 1)

print(N - max(lis))
