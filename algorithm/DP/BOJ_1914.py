import sys
sys.stdin = open('../input.txt', 'r')

circle_num = int(input())
k = 2 ** circle_num - 1
print(k)
if circle_num <= 20:
    dp = {i: {start: {end: [] for end in range(1, 4)} for start in range(1, 4)} for i in range(2)}
    dp[0][1][2].append('1 2')
    dp[0][1][3].append('1 3')
    dp[0][2][1].append('2 1')
    dp[0][2][3].append('2 3')
    dp[0][3][1].append('3 1')
    dp[0][3][2].append('3 2')
    for n in range(1, circle_num):
        dp[1][1][3] = dp[0][1][2] + ['1 3'] + dp[0][2][3]
        dp[1][1][2] = dp[0][1][3] + ['1 2'] + dp[0][3][2]
        dp[1][2][3] = dp[0][2][1] + ['2 3'] + dp[0][1][3]
        dp[1][2][1] = dp[0][2][3] + ['2 1'] + dp[0][3][1]
        dp[1][3][1] = dp[0][3][2] + ['3 1'] + dp[0][2][1]
        dp[1][3][2] = dp[0][3][1] + ['3 2'] + dp[0][1][2]
        dp[0][1][3] = dp[1][1][3][:]
        dp[0][1][2] = dp[1][1][2][:]
        dp[0][2][3] = dp[1][2][3][:]
        dp[0][2][1] = dp[1][2][1][:]
        dp[0][3][1] = dp[1][3][1][:]
        dp[0][3][2] = dp[1][3][2][:]
    print(*dp[0][1][3], sep='\n')
