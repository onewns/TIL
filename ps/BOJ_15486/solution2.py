import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


def solution(n, table):
    dp = [0] * (n + 1)
    for day in range(n-1, -1, -1):
        time, money = table[day]
        dp[day] = dp[day + 1]
        if time + day <= n:
            dp[day] = max(dp[day + 1], dp[day + time] + money)
    return dp[0]


if __name__ == '__main__':
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, arr))
