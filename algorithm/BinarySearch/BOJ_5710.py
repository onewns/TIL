import sys

sys.stdin = open('../input.txt', 'r')


def cal(n: int) -> int:
    if n > 1000000:
        return (n - 1000000) * 7 + 4979900
    elif n > 10000:
        return (n - 10000) * 5 + 29900
    elif n > 100:
        return (n - 100) * 3 + 200
    else:
        return n * 2


def howmuch(start: int, end: int) -> int:
    left, right = start, end
    while left <= right:
        mid = (left + right) // 2
        d = cal(total_electricity - mid) - cal(mid)
        if d == diff:
            return cal(mid)
        elif d > diff:
            left = mid + 1
        else:
            right = mid - 1


def electricity(m):
    if m > 4979900:
        return (m - 4979900) // 7 + 1000000
    elif m > 29900:
        return (m - 29900) // 5 + 10000
    elif m > 200:
        return (m - 200) // 3 + 100
    else:
        return m // 2


while True:
    total, diff = map(int, input().split())
    if not total and not diff:
        break
    total_electricity = electricity(total)
    print(howmuch(0, total_electricity // 2))
