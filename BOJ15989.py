# 1, 2, 3 더하기 4 - 실버 1
# 다이나믹 프로그래밍

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for k in range(int(input())):
    print(dp[int(input())])
