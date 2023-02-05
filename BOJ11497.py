# 통나무 건너뛰기 - 실버 1

for __ in range(int(input())):
    N = int(input())
    log = [*map(int, input().split())]
    log.sort()
    result = 0
    for i in range(N - 2):
        result = max(result, abs(log[i + 2] - log[i]))
    print(result)
