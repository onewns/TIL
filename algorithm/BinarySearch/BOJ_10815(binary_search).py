import sys
sys.stdin = open('../input.txt', 'r')


def binary_search(num, start, end):
    left, right = start, end - 1
    mid = (left + right) // 2
    if left > right:
        return 0
    if num == cards[mid]:
        return 1
    elif num > cards[mid]:
        return binary_search(num, mid + 1, end)
    else:
        return binary_search(num, left, mid)


n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
check_list = list(map(int, input().split()))
ans = []
for cn in check_list:
    ans.append(binary_search(cn, 0, n))
print(*ans)
