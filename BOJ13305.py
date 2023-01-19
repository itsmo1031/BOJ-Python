# 주유소 - 실버 3

n = int(input())
roads = [*map(int, input().split())]
prices = [*map(int, input().split())]

before = 0
cost = 0

for i in range(1, n):
    now = i
    if prices[now] < prices[before] or now == n - 1:
        cost += prices[before] * sum(roads[before:now])
        before = now

print(cost)
