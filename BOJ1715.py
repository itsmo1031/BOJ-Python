# 카드 정렬하기 - 골드 4

import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

result = 0

while len(cards) > 1:
    process = heapq.heappop(cards) + heapq.heappop(cards)
    result += process
    heapq.heappush(cards, process)

print(result)
