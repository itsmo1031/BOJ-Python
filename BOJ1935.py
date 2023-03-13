# 후위 표기식2 - 실버 3
# Stack

N = int(input())
exp = [*input()]
num = [float(input()) for __ in range(N)]
stack = []

for e in exp:
    if e not in "+-*/":
        stack.append(num[ord(e) - ord('A')])
    else:
        num2 = str(stack.pop())
        num1 = str(stack.pop())
        stack.append(eval(num1 + e + num2))

print(format(stack.pop(), '.2f'))
