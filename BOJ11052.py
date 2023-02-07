# 카드 구매하기 - 실버 1

N = int(input())
card = [0]
card.extend([*map(int, input().split())])

# 점화식: N번째 카드를 살때 최대값
# max(card[n-0]+card[0], card[n-1]+card[1],...,card[n-m] + card[m])
for i in range(2, N + 1):
    # 절반 이후로 같아지므로 (card[n-m]+card[m] == card[m]+card[n-m] 절반+1만큼만 확인
    for j in range(0, i // 2 + 1):
        card[i] = max(card[i], card[i - j] + card[j])

print(card[N])
