# 숫자 고르기 - 골드 5

N = int(input())

# 숫자 입력을 받을 2차원 리스트 선언
graph = [[] for __ in range(N + 1)]

for k in range(1, N + 1):
    graph[int(input())].append(k)  # 단방향 그래프로 표현

# 방문 여부 측정을 위한 check 리스트 선언
check = [False] * (N + 1)

# 결과값을 담기 위한 빈 리스트 선언
result = []


def dfs(i: int, cycle: set):
    check[i] = True
    cycle.add(i)
    # 해당 노드에 이어진 모든 간선에 대해 확인
    for v in graph[i]:
        # 그 값이 사이클에 존재하면 사이클을 결과값에 추가
        if v in cycle:
            result.extend(cycle)
        else:
            dfs(v, cycle.copy())


# 모든 그래프 정점에 대해서 dfs 수행
for x in range(1, N + 1):
    if not check[x]:
        dfs(x, set())

# 결과 출력
print(len(result))
for r in sorted(result):
    print(r)
