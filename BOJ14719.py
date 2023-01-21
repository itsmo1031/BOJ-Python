# 빗물 - 골드 5

h, w = map(int, input().split())
points = []
columns = [*map(int, input().split())]

for i in range(w):
    if columns[i] > 0:
        for j in range(columns[i]):
            points.append((i, j))

points.sort(key=lambda x: x[1])

result = 0
for i in range(len(points)-1):
    if points[i][1] != points[i+1][1]:
        continue
    result += points[i+1][0] - points[i][0] - 1

print(result)
