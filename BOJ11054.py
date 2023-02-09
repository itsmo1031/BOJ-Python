# 가장 긴 바이토닉 부분 수열 - 골드 4
"""
Concept
주어진 수열과 뒤집은 수열의 LIS+마지막까지의 LDS 를 각각 구해서 비교
"""

N = int(input())
A = [*map(int, input().split())]
B = A[::-1]


def find_bitonic(arr):
    # Find LIS
    lis = [1] * N

    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    # Find LIS from max_idx to the end of Array
    max_idx = arr.index(max(arr))

    for i in range(max_idx + 1, N):
        for j in range(max_idx, i):
            if arr[i] < arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)


print(max(find_bitonic(A), find_bitonic(B)))
