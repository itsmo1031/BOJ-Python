# 임스와 함께하는 미니게임 - 실버 5
N, G = input().split()
player = set()
for __ in range(int(N)):
    player.add(input())

print(len(player) // "_YFO".index(G))
