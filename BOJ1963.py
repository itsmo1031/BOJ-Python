from collections import deque
import sys

input = sys.stdin.readline
T = int(input())

n = 9999
primes = [True] * (n + 1)

for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
        for j in range(i + i, n + 1, i):
            primes[j] = False


def bfs(now, tobe):
    visited = [False] * 10000
    q = deque([[now, 0]])
    visited[now] = True
    while q:
        temp, cnt = q.popleft()
        if temp == tobe:
            return cnt
        temp = str(temp)
        for k in range(4):
            for w in range(10):
                new_num = int(temp[:k] + str(w) + temp[k + 1:])
                if not visited[new_num] and primes[new_num] and new_num >= 1000:
                    visited[new_num] = True
                    q.append([new_num, cnt + 1])
    return "Impossible"


for __ in range(T):
    A, B = map(int, input().split())
    answer = bfs(A, B)
    print(answer)
