# 거스름돈 - 브론즈 2
coins = [500, 100, 50, 10, 5, 1]
n = 1000 - int(input())
result = 0
for coin in coins:
    if n // coin > 0:
        result += n // coin
        n %= coin

print(result)
