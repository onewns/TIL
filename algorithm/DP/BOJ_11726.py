import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
dp = [0, 1, 2, 3]
now = 4
while now <= n:
    dp.append((dp[now - 1] + dp[now - 2]) % 10007)
    now += 1
print(dp[n])
