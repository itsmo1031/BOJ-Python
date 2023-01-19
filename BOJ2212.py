# 센서 - 골드 5
n = int(input())
k = int(input())
s = [*map(int, input().split())]
distance = []
s.sort()

for i in range(n - 1):
    distance.append(abs(s[i] - s[i + 1]))
distance.sort()

for _ in range(k - 1):
    if distance:
        distance.pop()
    else:
        break

print(sum(distance))
