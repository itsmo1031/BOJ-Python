# 비밀 모임 - 골드 4

INF = int(1e9)

for __ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    for __ in range(M):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    for i in range(1, N + 1):
        graph[i][i] = 0

    # 플로이드 워셜
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 친구 수와 방 번호 입력
    K = int(input())
    friend = [*map(int, input().split())]

    result = 0
    min_dist = INF
    for i in range(1, N + 1):
        temp = 0
        for f in friend:
            temp += graph[f][i]
        if temp < min_dist:
            min_dist = temp
            result = i

    print(result)