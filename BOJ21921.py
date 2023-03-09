# 블로그 - 실버 3
# 슬라이딩 윈도우

N, X = map(int, input().split())
visit = [*map(int, input().split())]
start = now = result = cnt = 0

for i, v in enumerate(visit):
    now += v
    if i - start + 1 == X:
        if result == now:
            cnt += 1
        elif result < now:
            cnt = 1
            result = now
        now -= visit[start]
        start += 1

if result != 0:
    print(result)
    print(cnt)
else:
    print("SAD")
