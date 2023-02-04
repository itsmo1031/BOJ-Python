# 스네이크버드 - 실버 5

N, L = map(int, input().split())

fruit = [*map(int, input().split())]
fruit.sort(reverse=True)

while fruit:
    f = fruit.pop()
    if L < f:
        break
    L += 1

print(L)
