import sys
sys.stdin = open('../input.txt', 'r')


def what_num(n):
    if len(memo) <= n:
        memo.append(what_num(n - 3) + what_num(n - 2) + what_num(n - 1))
    return memo[n]


def what_num_2(n):
    now = len(memo)
    while now <= n:
        memo.append(memo[now - 1] + memo[now - 2] + memo[now - 3])
        now += 1
    return memo[n]


memo = [0, 1, 2, 4, 7]
for _ in range(int(input())):  # 사실상 피보나치
    print(what_num_2(int(input())))
    print(what_num(int(input())))