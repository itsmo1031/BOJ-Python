# 신입 사원 - 실버 1 재풀이

for _ in range(int(input())):
    n = int(input())
    scores = []
    for _ in range(n):
        scores.append(tuple(map(int, input().split())))

    scores.sort()
    base = scores[0][1]
    count = 0
    for score in scores:
        if score[1] <= base:
            count += 1
            base = score[1]
    print(count)
