# 회의실 배정 - 실버 1
import sys

n = int(input())
meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

before = meetings[0]
result = 1

for i in range(1, n):
    if meetings[i][0] >= before[1]:
        result += 1
        before = meetings[i]

print(result)
