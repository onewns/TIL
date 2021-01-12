import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
nums = sorted(list(map(int, input().split())))
target = int(input())
ans = 0
left, right = 0, n - 1
while left < right:
    now = nums[left] + nums[right]
    if now == target:
        ans += 1
        left += 1
    elif now > target:
        right -= 1
    else:
        left += 1
print(ans)
