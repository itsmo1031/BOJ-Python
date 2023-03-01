# 스타트와 링크 - 실버 2
from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())
S = [[*map(int, input().split())] for __ in range(N)]


def calc_stat(team):
    res = 0
    for x, y in combinations(team, 2):
        res += S[x][y] + S[y][x]
    return res


result = int(1e9)
for start in combinations(range(N), N // 2):
    link = tuple(filter(lambda x: x not in start, range(N)))
    result = min(result, abs(calc_stat(start) - calc_stat(link)))

print(result)
