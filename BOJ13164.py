# 행복 유치원 - 골드 5

N, K = map(int, input().split())

# 원생 정보 입력
arr = [*map(int, input().split())]

diff = []

for i in range(N - 1):
    diff.append(arr[i + 1] - arr[i])

diff.sort()

print(sum(diff[:N - K]))
