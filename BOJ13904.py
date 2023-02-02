# 과제 - 골드 3
# TODO: 우선순위 큐로 풀어보기

N = int(input())

todo = []
for __ in range(N):
    todo.append(tuple(map(int, input().split())))

todo.sort(reverse=True)
deadline = todo[0][0]
score = 0

while deadline:
    cand = [*filter(lambda x: x[0] >= deadline, todo)]
    if cand:
        res = max(cand, key=lambda x: x[1])
        score += res[1]
        todo.remove(res)
    deadline -= 1

print(score)
