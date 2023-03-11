# 초콜릿 식사 - 실버 2

K = int(input())

size = 1  # 초콜릿 사이즈 선언
cnt = 0  # 쪼갤 횟수 변수 선언

while size < K:
    size <<= 1  # 비트 연산 (왼쪽으로 한칸씩 움직일수록 2배 증가)

result = size

while K:
    if K >= size:
        K -= size
    else:
        size //= 2
        cnt += 1

print(result, cnt)
