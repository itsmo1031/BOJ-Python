# 잃어버린 괄호 - 실버 2
from functools import reduce

subs = [*map(str, input().split('-'))]
final = []
for sub in subs:
    final.append(sum(map(int, sub.split('+'))))

print(reduce(lambda x, y: x - y, final))
