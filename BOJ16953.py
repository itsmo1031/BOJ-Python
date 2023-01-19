# A -> B - 실버 2
a, b = input().split()

result = 1

while int(a) != int(b):
    if int(b) < int(a):
        result = -1
        break
    if b[-1] == '1':
        b = b[:len(b) - 1]
        result += 1
    else:
        if int(b) % 2 == 1:
            result = -1
            break
        b = str(int(b) // 2)
        result += 1

print(result)
