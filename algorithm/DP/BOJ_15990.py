import sys
sys.stdin = open('../input.txt', 'r')


def th_recur(n):
    if len(dp) <= n:
        dp.append([(sum(th_recur(n - 1)) - th_recur(n - 1)[0]) % 1000000009,
                   (sum(th_recur(n - 2)) - th_recur(n - 2)[1]) % 1000000009,
                   (sum(th_recur(n - 3)) - th_recur(n - 3)[2]) % 1000000009])
    return dp[n]


def three_loop(n):
    now = len(dp)
    while now <= n:
        dp.append([(sum(dp[now - 1]) - dp[now - 1][0]) % 1000000009,
                   (sum(dp[now - 2]) - dp[now - 2][1]) % 1000000009,
                   (sum(dp[now - 3]) - dp[now - 3][2]) % 1000000009])
        now += 1
    return dp[n]


dp = [[0], [1, 0, 0], [0, 1, 0], [1, 1, 1], [2, 0, 1]]
for _ in range(int(input())):
    print(sum(three_loop(int(sys.stdin.readline()))) % 1000000009)