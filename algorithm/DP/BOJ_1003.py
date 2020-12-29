import sys
sys.stdin = open('../input.txt', 'r')


def call_num_re(n):
    if len(memo) <= n:
        memo.append([call_num_re(n - 1)[0] + call_num_re(n - 2)[0], call_num_re(n - 1)[1] + call_num_re(n - 2)[1]])
    return memo[n]


def call_num_loop(n):
    now = len(memo)
    while now <= n:
        memo.append([memo[now-1][0] + memo[now-2][0], memo[now-1][1] + memo[now-2][1]])
        now += 1
    return memo[n]


memo = [[1, 0], [0, 1]]
for tc in range(int(input())):
    n = int(input())
    print(*call_num_loop(n))
    print(*call_num_re(n))
