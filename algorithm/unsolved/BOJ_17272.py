import sys
sys.stdin = open('../input.txt', 'r')


t1, t2 = map(int, input().split())
dp = [1 for _ in range(t2)]
while t1 >= len(dp):
    dp.append((dp[-1] + dp[len(dp) - t2]) % 1000000007)
print(dp[-1])

n = 1000000000000000000
while n > 1:
    n //= 2
    print(n)