import sys
sys.stdin = open('../input.txt', 'r')


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
dp = [list([0, 0, 0] for _ in range(size)) for _ in range(size)]
for x in range(1, size):
    if matrix[0][x]:
        break
    dp[0][x][0] = 1
for idy in range(1, size):
    for idx in range(1, size):
        if not matrix[idy][idx]:
            dp[idy][idx][0] = dp[idy][idx-1][0] + dp[idy][idx-1][2]
            dp[idy][idx][1] = dp[idy-1][idx][1] + dp[idy-1][idx][2]
            if not matrix[idy-1][idx] and not matrix[idy][idx-1]:
                dp[idy][idx][2] = sum(dp[idy-1][idx-1])
print(sum(dp[-1][-1]))
