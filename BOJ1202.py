# 보석 도둑 - 골드 4
import heapq
import sys

n, k = map(int, sys.stdin.readline().split())
gems = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    gems.append((m, v))
gems.sort()
bags = []
for _ in range(k):
    heapq.heappush(bags, int(sys.stdin.readline()))

result = 0
idx = 0
selected = []

while bags:
    bag = heapq.heappop(bags)  # 가장 작은 가방 뽑기
    while idx < n and bag >= gems[idx][0]:  # 가방 크기에 맞는 보석 넣기 (다음 가방이 와도 현재 가방 크기보다 크기 때문에 selected에 넣었던 보석들은 다 들어감)
        heapq.heappush(selected, -gems[idx][1])
        idx += 1
    if selected:
        result -= heapq.heappop(selected)

print(result)
