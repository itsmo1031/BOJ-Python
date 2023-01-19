# ATM - 실버 4
n = int(input())
p = [*map(int, input().split())]
p.sort()

result = 0
print(sum(map(lambda x, y: x * y, p, range(len(p), 0, -1))))
