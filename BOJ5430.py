# AC - 골드 5
# TODO: ast와 deque없이 풀이해보기

import ast
from collections import deque


def do_ac(commands, ln, li):
    r_idx = 0
    for c in commands:
        if c == 'R':
            r_idx = (r_idx + 1) % 2
        if c == 'D':
            try:
                if r_idx % 2 == 1:
                    li.pop()
                else:
                    li.popleft()
            except IndexError:
                return 'error'
    return '[' + ','.join(map(str, li)) + ']' if r_idx % 2 == 0 else '[' + ','.join(map(str, reversed(li))) + ']'


for _ in range(int(input())):
    p = input()
    n = int(input())
    ns = deque(ast.literal_eval(input()))
    print(do_ac(p, n, ns))
