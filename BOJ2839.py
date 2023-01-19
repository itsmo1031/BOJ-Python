# 설탕 배달 - 실버 4
# n이 3x+5y=n을 만족하는가?

n = int(input())

result = 0
cnt = 0

while n >= 0:
    if n % 5 == 0:
        result = cnt + n // 5
        break
    else:
        cnt += 1
        n -= 3
if n < 0:
    result = -1

print(result)
