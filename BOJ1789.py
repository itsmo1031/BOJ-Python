# 수들의 합 - 실버 5
s = int(input())
idx = 0
cnt = 0
while s > idx:
    idx += cnt + 1
    cnt += 1
result = 0
if s == idx:
    result = cnt
else:
    result = cnt - 1

print(result)
