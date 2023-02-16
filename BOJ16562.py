# 친구비 - 골드 4
import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if cost[x] <= cost[y]:
        parent[y] = x
    else:
        parent[x] = y


N, M, k = map(int, input().split())
cost = [0] + [*map(int, input().split())]
parents = [*range(N + 1)]

for __ in range(M):
    v, w = map(int, input().split())
    union_parent(parents, v, w)

result = 0
for idx, root in enumerate(parents):
    if idx == root:
        result += cost[idx]

if result <= k:
    print(result)
else:
    print("Oh no")
