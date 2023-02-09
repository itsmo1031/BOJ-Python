# 파이프 옮기기 1 - 골드 5

N = int(input())

# 벽 있는 보드로 만들기
board = [[1] * (N + 2) for __ in range(N + 2)]
for i in range(N):
    temp = [*map(int, input().split())]
    for j in range(N):
        board[i + 1][j + 1] = temp[j]

# 끝점이 가로, 세로, 대각선 순인 dp 테이블 선언
dp = [[[0, 0, 0] for _ in range(N + 2)] for _ in range(N + 2)]

# 최초 값 설정
dp[1][2][0] = 1

# (1,1)부터 (N,N)까지 순회
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # 가로일때
        if dp[i][j][0]:
            if board[i][j + 1] != 1:
                # 가로 가짓수 추가
                dp[i][j + 1][0] += dp[i][j][0]
                # 대각선 가짓수 추가
                if board[i + 1][j + 1] != 1 and board[i + 1][j] != 1:
                    dp[i + 1][j + 1][2] += dp[i][j][0]
        # 세로일때
        if dp[i][j][1]:
            if board[i + 1][j] != 1:
                # 세로 가짓수 추가
                dp[i + 1][j][1] += dp[i][j][1]
                # 대각선 가짓수 추가
                if board[i + 1][j + 1] != 1 and board[i][j + 1] != 1:
                    dp[i + 1][j + 1][2] += dp[i][j][1]
        # 대각선일때
        if dp[i][j][2]:
            # 가로 가짓수 추가
            if board[i][j + 1] != 1:
                dp[i][j + 1][0] += dp[i][j][2]
            # 세로 가짓수 추가
            if board[i + 1][j] != 1:
                dp[i + 1][j][1] += dp[i][j][2]
            # 대각선 가짓수 추가
            if board[i][j + 1] != 1 and board[i + 1][j] != 1 and board[i + 1][j + 1] != 1:
                dp[i + 1][j + 1][2] += dp[i][j][2]

print(sum(dp[N][N]))
