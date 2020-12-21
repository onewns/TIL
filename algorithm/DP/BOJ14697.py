import sys
sys.stdin = open("../input.txt", 'r')


def is_possible(input_data):
    r1, r2, r3, people = input_data
    dp = [0 for _ in range(301)]
    dp[r1], dp[r2], dp[r3] = 1, 1, 1
    for person in range(1, people + 1):
        if dp[person] or dp[person - r1] or dp[person - r2] or dp[person - r3]:
            dp[person] = 1
        else:
            dp[person] = 0
    return dp[people]


print(is_possible(map(int, input().split())))