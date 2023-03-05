# 저울 - 골드 4
# 플로이드 워셜

INF = int(1e9)
N = int(input())

weight = [[INF] * N for __ in range(N)]

for i in range(N):
    weight[i][i] = 0

for __ in range(int(input())):
    a, b = map(int, input().split())
    weight[a - 1][b - 1] = 1

# 플로이드 워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            weight[i][j] = min(weight[i][j], weight[i][k] + weight[k][j])

# 플로이드 워셜 수행 후, 그래프를 대칭으로 수행
# 위처럼 플로이드 워셜을 수행하면 a>b>c와 같이 무거운 무게밖에 판별하지 못함.
# 반면 우리가 알아야 하는 정보는 무게의 정보가 아닌 "비교 결과를 알 수 있는지"이므로,
# 그래프를 대칭하여 둘 중의 최솟값으로 바꿔주면 비교 결과를 알 수 있는 그래프로 바뀜.
# ex) 1>2는 알지만 2>1은 입력되어있지 않으므로 weight[2][1]의 값이 INF였지만,
# 아래의 연산을 수행하면 weight[2][1]의 값이 weight[1][2]값과 같아져 비교 가능하다고 판별할 수 있음.
for i in range(N):
    for j in range(N):
        if weight[i][j] == INF:
            weight[i][j] = min(weight[i][j], weight[j][i])

for w in weight:
    print(w.count(INF))
