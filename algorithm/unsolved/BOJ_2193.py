import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
dp = [0, 1, 1, 2, 3, 5]
while len(dp) <= n:
    dp.append(dp[len(dp)-1] + dp[len(dp)-2])
print(dp[n])
