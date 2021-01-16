import sys
sys.stdin = open('../input.txt', 'r')


dp = [0, 0, 3, 0, 11]
n = int(input())
while len(dp) <= n:
    if len(dp) % 2:
        dp.append(0)
    else:
        dp.append(2 + dp[len(dp) - 2] + 2 * sum(dp))
print(dp[n])
