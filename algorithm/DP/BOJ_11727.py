import sys
sys.stdin = open('../input.txt', 'r')


def tiling_recursion(num):
    if len(memo) <= num:
        memo.append((tiling_recursion(num - 1) + tiling_recursion(num - 2) * 2) % 10007)
    return memo[num]


def tiling_loop(num):
    now = len(dp)
    while now <= num:
        dp.append((dp[now - 1] + 2 * dp[now - 2]) % 10007)
        now += 1
    return dp[num]


dp = [0, 1, 3]
memo = [0, 1, 3]
n = int(input())
print(tiling_loop(n))
print(tiling_recursion(n))
