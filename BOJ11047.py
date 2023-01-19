# 동전 0 - 실버 4

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
result = 0
for coin in coins:
    if k == 0:
        break
    if k // coin > 0:
        result += k // coin
        k = k % coin

print(result)
