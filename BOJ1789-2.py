# 수들의 합 - 실버 5
# 가우스 덧셈으로 풀이

s = int(input())
idx = 1
while (1 + idx) * idx / 2 <= s:
    idx += 1
if (1 + idx) * idx / 2 > s:
    print(idx - 1)
else:
    print(idx)
