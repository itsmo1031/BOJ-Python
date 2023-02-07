# 가장 긴 증가하는 부분 수열 - 실버 2

N = int(input())
arr = [*map(int, input().split())]
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
