# 삼각형 만들기 - 실버 3
import sys

input = sys.stdin.readline
N = int(input())
straw = []
for __ in range(N):
    straw.append(int(input()))

straw.sort(reverse=True)
result = -1

for i in range(N - 2):
    if straw[i] < sum(straw[i + 1:i + 3]):
        result = sum(straw[i:i + 3])
        break

print(result)
