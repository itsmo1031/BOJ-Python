# 강의실 배정 - 골드 5
# 관건: 시간 복잡도

import heapq

n = int(input())
classes = []
for _ in range(n):
    classes.append(tuple(map(int, input().split())))
classes.sort()
end_times = []

for c in classes:
    if len(end_times) == 0 or c[0] < end_times[0]:
        heapq.heappush(end_times, c[1])
    else:
        heapq.heapreplace(end_times, c[1])

result = len(end_times)
print(result)

"""
heapq 없이 푸는 과정 - 수학적 사고력 필요
"""

# N = int(input())
# classes = []
# for i in range(N):
#     start_time, end_time = map(int, input().split())
#     classes += [(start_time, 1), (end_time, -1)]
# classes.sort()
#
# result = c = 0
# for time, trigger in classes:
#     c += trigger
#     result = max(result, c)
#
# print(result)
