# 30 - 실버 4
# 3의 배수이면서 10의 배수인 수
# 3의 배수: 각 자리수를 더해서 3의 배수
# 10의 배수: 끝자리 0
from functools import reduce

n = input()

if n.find('0') == -1:
    result = -1
else:
    tmp = reduce(lambda x, y: int(x) + int(y), n)
    if tmp % 3 == 0:
        result = ''.join(sorted(n)[::-1])
    else:
        result = -1

print(result)
