# PPAP - 골드 4
import sys

words = sys.stdin.readline().rstrip()

s = []
ppap = [*'PPAP']
for word in words:
    s.append(word)
    if s[-4:] == ppap:
        for _ in range(3):
            s.pop()
if s == ['P']:
    print('PPAP')
else:
    print('NP')
