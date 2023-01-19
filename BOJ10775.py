# 공항 - 골드 2
import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
airport = {x: 0 for x in range(1, g + 1)}
result = 0

for _ in range(g):
    plane = int(sys.stdin.readline())
    land = False
    for i in range(plane, 0, -1):
        if airport[i] == 0:
            airport[i] = plane
            land = True
            result += 1
            break
    if not land:
        break

print(result)
