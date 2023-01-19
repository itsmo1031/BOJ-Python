# 저울 - 골드 2
# 수직선을 생각하자

n = int(input())
weights = [*map(int, input().split())]
weights.sort()

result = 1

for weight in weights:
    if weight > result:
        break
    result += weight

print(result)
