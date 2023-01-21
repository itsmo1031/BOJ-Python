# 괄호의 값 - 실버 1
# TODO: 설명 없이 다시 한 번 풀어보기

brackets = input()
tmp = 1
result = 0
stack = []

for i in range(len(brackets)):
    b = brackets[i]
    if b == '(':
        tmp *= 2
        stack.append(b)
    elif b == '[':
        tmp *= 3
        stack.append(b)
    elif b == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if brackets[i-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop()
    elif b == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if brackets[i-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop()
    else:
        result = 0
        break

print(result if not stack else 0)
