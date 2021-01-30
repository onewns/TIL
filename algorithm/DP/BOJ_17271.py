import sys
sys.stdin = open('../input.txt', 'r')


n, m = map(int, input().split())
if n < m:
    print(1)
else:
    dp = [1] * (m+1)
    dp[-1] += 1
    now = len(dp)
    while now <= n:
        dp.append((dp[now-1] + dp[now-m]) % 1000000007)
        now += 1
    print(dp[-1])
