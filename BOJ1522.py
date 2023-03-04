# 문자열 교환 - 실버 1
# 슬라이딩 윈도우 알고리즘 이용

arr = input()
cnt_a = arr.count("a")
arr *= 2
answer = 1001

for i in range(len(arr) - cnt_a + 1):
    now = arr[i:i + cnt_a]
    answer = min(answer, now.count("b"))

print(answer)
