# 배 - 골드 5
n = int(input())
cranes = [*map(int, input().split())]
cranes.sort(reverse=True)
m = int(input())
boxes = [*map(int, input().split())]
boxes.sort(reverse=True)

result = 0

if cranes[0] < boxes[0]:
    print(-1)
else:
    while boxes:
        for i in range(len(cranes)):
            for j in range(len(boxes)):
                if cranes[i] >= boxes[j]:
                    boxes.pop(j)
                    break
        result += 1
    print(result)
