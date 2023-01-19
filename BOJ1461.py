# 도서관 - 골드 5
n, m = map(int, input().split())
b = [*map(int, input().split())]
minus = sorted([-x for x in filter(lambda x: x < 0, b)])
plus = sorted([*filter(lambda x: x > 0, b)])
max_num = max(minus + plus)


def clean(books):
    result = 0
    while books:
        i = books.pop()
        for _ in range(m - 1):
            if books:
                books.pop()
        result += i if i == max_num else i * 2
    return result


print(clean(minus) + clean(plus))
