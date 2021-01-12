import sys
sys.stdin = open('../input.txt', 'r')


def binary_search(n, start, end):
    left, right = start, end - 1
    while left <= right:
        mid = (left + right) // 2
        if n == nums[mid]:
            return True
        elif n < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1


n = int(input())
nums = sorted(list(map(int, input().split())))
target = int(input())
ans = 0
for s in range(n - 1):
    if binary_search(target - nums[s], s + 1, n):
        ans += 1
print(ans)
