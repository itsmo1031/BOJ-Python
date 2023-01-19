# 신입 사원 - 실버 1

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    scores = []
    for _ in range(n):
        scores.append(tuple(map(int, sys.stdin.readline().split())))
    base = (min(scores, key=lambda x: x[1])[0], min(scores)[1])

    print(len([x for x in scores if x[0] <= base[0] and x[1] <= base[1]]))

# 틀림 -> 반례
# 1
# 5
# 1 5
# 5 1
# 2 2
# 3 3 
# 4 4
