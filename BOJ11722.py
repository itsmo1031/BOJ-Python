# 가장 긴 감소하는 부분 수열 - 실버 2

N = int(input())
arr = [*map(int, input().split())]

lds = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] > arr[i]:
            lds[i] = max(lds[i], lds[j] + 1)

print(max(lds))
