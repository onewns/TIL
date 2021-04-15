import sys
sys.stdin = open('../input.txt', 'r')


def get_max(n):
    if n & 1:
        return '7' + '1' * ((n-2) // 2)
    return '1' * (n // 2)


def solution(n):
    dp = {1: '0', 2: '1', 3: '7', 4: '4', 5: '2', 6: '6', 7: '8', 8: '10'}
    cur = 9
    while cur <= n:
        dp[cur] = min(
            dp[cur - 2] + '1',
            '1' + dp[cur - 2],
            dp[cur - 3] + '7',
            '7' + dp[cur - 3],
            dp[cur - 4] + '4',
            '4' + dp[cur - 4],
            dp[cur - 5] + '2',
            '2' + dp[cur - 5],
            dp[cur - 6] + '0',
             '6' + dp[cur - 6],
             dp[cur - 7] + '8',
             '8' + dp[cur - 7],
            key=lambda x: (len(x), x))
        cur += 1
    return [int(dp[n]), int(get_max(n))]


for _ in range(int(input())):
    print(*solution(int(input())))