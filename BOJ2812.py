# 크게 만들기 - 골드 3
n, k = map(int, input().split())
max_len = n - k
s = input()
t = s.index(max(s[:k + 1]))
k -= t
nums = s[t:]
result = []

for num in nums:
    if k == 0 or not result:
        result.append(num)
    else:
        for i in range(k):
            if num > result[len(result) - 1]:
                result.pop()
                k -= 1
            else:
                break
        result.append(num)
    if len(result) > max_len:
        result.pop()
        k -= 1

print(''.join(result))
