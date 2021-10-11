import sys
sys.stdin = open('../input.txt', 'r')

n = int(input())
nums = list(map(int, input().split()))
target = nums.pop()
dp = [[0] * 21]
dp[0][nums[0]] += 1
now = 1
while now < n - 1:
    temp = [0] * 21
    num = nums[now]
    for i in range(21):
        if 0 <= i + num <= 20:
            temp[i + num] += dp[-1][i]
        if 0 <= i - num <= 20:
            temp[i - num] += dp[-1][i]
    dp.append(temp)
    now += 1
print(dp[-1][target])
