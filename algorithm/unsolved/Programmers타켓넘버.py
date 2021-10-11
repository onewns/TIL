"""
오후 5시 10분
오후 5시 35분
"""


# def dfs(depth, nums, temp, target):
#     ans = 0
#     if abs(target - temp) > sum(nums[depth:]):
#         return 0
#     if depth == len(nums):
#         if temp == target:
#             return 1
#         return 0
#     else:
#         ans += dfs(depth + 1, nums, temp + nums[depth], target)
#         ans += dfs(depth + 1, nums, temp - nums[depth], target)
#     return ans
#
#
def solution(numbers, target):
    total = sum(numbers)
    # ans = dfs(0, numbers, 0, target)
    dp = [{0: 1}]
    for i in range(len(numbers)):
        dp.append({})
        for j in dp[i].keys():
            if dp[i][j]:
                if j + numbers[i] not in dp[i + 1]:
                    dp[i + 1][j + numbers[i]] = dp[i][j]
                else:
                    dp[i + 1][j + numbers[i]] += dp[i][j]
                if j - numbers[i] not in dp[i + 1]:
                    dp[i + 1][j - numbers[i]] = dp[i][j]
                else:
                    dp[i + 1][j - numbers[i]] += dp[i][j]
    # return ans
    return dp[-1][target]


print(solution([1, 1, 1, 1, 1], 3))
