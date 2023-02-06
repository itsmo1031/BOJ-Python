# 1,2,3 더하기 - 실버 3

case = [0] * 10

case[0] = 1
case[1] = 2
case[2] = 4

for i in range(3, 10):
    case[i] = sum(case[i - 3:i])

for __ in range(int(input())):
    print(case[int(input()) - 1])
