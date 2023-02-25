# 알약 - 골드 5

dp = [[0] * 31 for __ in range(31)]

for i in range(1, 31):
    dp[0][i] = 1
for i in range(1, 31):
    for j in range(30):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        else:
            dp[i][j] = dp[i - 1][j + 1] + dp[i][j - 1]

while True:
    P = int(input())
    if P == 0:
        break
    print(dp[P][0])
