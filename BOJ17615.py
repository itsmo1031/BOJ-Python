# 볼 모으기 - 실버 1

N = int(input())
ball = input()
current = ""
balls = []
cnt = 1
for b in ball:
    if current != b:
        if current != "":
            balls.append(current * cnt)
            cnt = 1
        current = b
    else:
        cnt += 1
balls.append(current * cnt)

red = ball.count("R")
blue = ball.count("B")
result = N
if "R" in balls[0]:
    result = min(result, red - len(balls[0]), blue)
else:
    result = min(result, red, blue - len(balls[0]))
if "R" in balls[-1]:
    result = min(result, red - len(balls[-1]), blue)
else:
    result = min(result, red, blue - len(balls[-1]))

print(result)
