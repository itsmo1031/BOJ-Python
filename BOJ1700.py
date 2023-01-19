# 멀티탭 스케줄링 - 골드 1
from collections import deque

n, k = map(int, input().split())
items = deque(map(int, input().split()))
multi = []
cnt = 0
idx = []

while items:
    item = items.popleft()
    if item in multi:
        continue
    if len(multi) < n:
        multi.append(item)
    else:
        idx.clear()
        for i in multi:
            try:
                idx.append(items.index(i))
            except ValueError:
                idx.append(101)
        multi[idx.index(max(idx))] = item  # 제일 멀리 떨어져 있는(다음에 쓸 순번이 제일 먼) 아이템을 교체
        cnt += 1

print(cnt)
