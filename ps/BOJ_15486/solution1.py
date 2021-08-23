import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def solution(day, table):
    dp = [0] * (day + 1)
    arr = {i: [] for i in range(1, day + 1)}
    for index, info in enumerate(table):
        time, money = info
        if index + time <= day:
            arr[index + time].append((time, money))
    for today in range(1, day + 1):
        new_money = 0
        for time, money in arr[today]:
            new_money = max(new_money, dp[today - time] + money)
        dp[today] = max(dp[today - 1], new_money)
    return dp[-1]


if __name__ == '__main__':
    N = int(input())
    array = [tuple(map(int, input().split())) for _ in range(N)]
    print(solution(N, array))
