# 수 묶기 - 골드 4

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

plus = [*filter(lambda x: x > 0, nums)]
minus = [*filter(lambda x: x <= 0, nums)]

# 큰 수부터 pop하기 위해 오름차순 정렬
plus.sort()
# 작은 수부터 pop하기 위해 내림차순 정렬
minus.sort(reverse=True)

bulk = []

while len(plus) > 1:
    a = plus.pop()
    b = plus.pop()
    bulk.append(a * b if a > 1 or b > 1 else a + b)  # 1이 2개 남았을 때 예외처리
while len(minus) > 1:
    bulk.append(minus.pop() * minus.pop())

result = sum(bulk + plus + minus)

print(result)
