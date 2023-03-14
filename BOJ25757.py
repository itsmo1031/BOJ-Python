# 임스와 함께하는 미니게임 - 실버 5
N, G = input().split()
player = set()
for __ in range(int(N)):
    player.add(input())

if G == 'Y':
    max_p = 1
elif G == 'F':
    max_p = 2
else:
    max_p = 3

print(len(player) // max_p)
