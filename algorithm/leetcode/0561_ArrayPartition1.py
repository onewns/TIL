# leetcode 561

class Solution:
    def arrayPairSum(self, nums) -> int:

        # my style 246ms 16.9MB
        nums = sorted(nums)
        ans = sum(nums[::2])
        return ans

        # use ascending 280ms 16.8MB
        s = 0
        pair = []
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                s += min(pair)
                pair = []
        return s

        # use even 276ms, 16.8MB
        s = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i % 2 == 0:
                s += n
        return s

        #use Pythonic Way
        return sum(sorted(nums)[::2])