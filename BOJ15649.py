# N과 M (1) - 실버 3
from itertools import permutations

N, M = map(int, input().split())
for p in permutations(range(1, N + 1), M):
    print(*p)
