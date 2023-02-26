# 두 배 더하기 - 골드 5
# 그리디 알고리즘 이용

N = int(input())
arr = [*map(int, input().split())]

cnt = 0

while True:
    trig = False
    if len(set(arr)) == 1 and 0 in arr:
        break
    for i in range(N):
        if arr[i] % 2 != 0:
            arr[i] -= 1
            trig = True
            break
    if not trig:
        arr = [*map(lambda x: x // 2, arr)]
    cnt += 1

print(cnt)
