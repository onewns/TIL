import sys
sys.stdin = open('../input.txt', 'r')


dp = [1, 1]
n = int(input())
now = 1
while now < n:
    dp.append((dp[now] + dp[now-1]) % 15746)
    now += 1
print(dp[-1])