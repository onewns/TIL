import sys
sys.stdin = open('../input.txt', 'r')


dp = [[0, 0], [0, 0]]
n = int(input())
for _ in range(n):
    score = int(input())
    dp.append([max(dp[-2]) + score, dp[-1][0] + score])
print(max(dp[-1]))
