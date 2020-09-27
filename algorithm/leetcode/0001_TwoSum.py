# leetcode 1
def twoSum(self, nums: List[int], target: int) -> List[int]:

    # my style 5356ms 15MB
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

    # use in 1044ms 14.9MB
    for i, num in enumerate(nums):
        second = target - num
        if second in nums[i+1:]:
            return i, nums[i+1:].index(second) + i + 1

    # use key 48ms 16.1MB
    dic = {}
    for i, num in enumerate(nums):
        dic[num] = i
    for i, num in enumerate(nums):
        if target - num in dic and i != dic[target-num]:
            return i, dic[target-num]

    # upgrade lookup 44ms, 15.3MB
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return dic[target-num], i
        dic[num] = i

    # use two pointer => require sort