import sys
sys.stdin = open('../input.txt', 'r')


dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for tc in range(int(input())):
    n = int(input())
    while len(dp) <= n:
        dp.append(dp[-1] + dp[-5])
    print(dp[n])
