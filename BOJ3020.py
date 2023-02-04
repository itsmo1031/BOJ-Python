# 개똥벌레 - 골드 5
# 이진 탐색

from bisect import bisect_left

N, H = map(int, input().split())
floor = []  # 석순 베얄
ceil = []  # 종유석 배열
for __ in range(N // 2):
    floor.append(int(input()))
    ceil.append(int(input()))

floor.sort()
ceil.sort()
result = N + 1
res_cnt = 0

for i in range(H):  # 모든 높이에 개똥벌레 보내서 확인
    # 석순 전체 개수(N//2)에서 이진 탐색 위치를 빼 주면 높이 i+1(1~H)일 때 부숴야 할 석순의 개수가 나옴
    floor_cnt = N // 2 - bisect_left(floor, i + 1)
    # 종유석도 마찬가지로 전체 개수에서 이진 탐색 위치를 빼주면 되는데, 이 때 높이는 석순의 반대인 H부터 1까지(H-i)가 되어야 함
    ceil_cnt = N // 2 - bisect_left(ceil, H - i)
    # 부숴야 할 석순의 개수와 종유석의 개수를 더함
    cnt = floor_cnt + ceil_cnt
    # 현재 부숴야할 개수가 결과값(현재 최소값)과 같으면 결과 카운트를 추가, 현재 최소값보다 방금 구한 값이 적다면 결과 리셋
    if cnt == result:
        res_cnt += 1
    if cnt < result:
        result = cnt
        res_cnt = 1

print(result, res_cnt)
