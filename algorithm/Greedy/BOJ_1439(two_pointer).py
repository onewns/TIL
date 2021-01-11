import sys
sys.stdin = open('../input.txt', 'r')


nums = input()
ans = 0
left, right = 0, len(nums) - 1
while left <= right:
    while left < right and nums[left] == nums[left + 1]:
        left += 1
    while left < right and nums[right] == nums[right - 1]:
        right -= 1
    if nums[left] != nums[right]:
        ans += 1
    left += 1
print(ans)