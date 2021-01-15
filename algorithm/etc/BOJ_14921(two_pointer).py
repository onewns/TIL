import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
nums = list(map(int, input().split()))
left, right = 0, n - 1
ans = float('inf')
while left < right:
    temp = nums[left] + nums[right]
    if temp == 0:
        print(0)
        break
    elif temp > 0:
        right -= 1
    else:
        left += 1
    if abs(ans) > abs(temp):
        ans = temp
else:
    print(ans)

