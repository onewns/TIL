import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

import random
# n, m = map(int, input().split())
# nums = [int(input()) for _ in range(n)]
n = 100000
nums = list(random.sample(range(1, 1000000000), n))
dp = [[(nums[i], nums[i])] for i in range(n)]
k = 1
for left_index in range(n):
    min_num, max_num = dp[left_index][0]
    for right_index in range(left_index + 1, n):
        min_num, max_num = min(min_num, nums[right_index]), max(max_num, nums[right_index])
        dp[left_index].append((min_num, max_num))
        print(k)
        k += 1
# print(dp)
