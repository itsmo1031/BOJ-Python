# 동전 - 골드 5

for __ in range(int(input())):
    N = int(input())
    coin = [*map(int, input().split())]
    M = int(input())
    dp = [0] * (M + 1)
    dp[0] = 1

    for i in range(N):
        for j in range(coin[i], M + 1):
            dp[j] += dp[j - coin[i]]

    print(dp[M])
