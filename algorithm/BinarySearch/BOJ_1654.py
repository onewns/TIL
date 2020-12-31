import sys
sys.stdin = open('../input.txt', 'r')


def howlong(start, end):
    left, right = start, end
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        nums = 0
        for line in lines:
            nums += (line // mid)
        if nums >= n:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans


k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
print(howlong(1, max(lines)))
