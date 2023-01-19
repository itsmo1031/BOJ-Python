# 보물 - 실버 4

n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

print(sum(map(lambda x, y: x * y, sorted(a), sorted(b, reverse=True))))
