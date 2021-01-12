import sys
sys.stdin = open('../input.txt', 'r')


levels = int(input())
scores = [int(input()) for _ in range(levels)]
ans = 0
for level in range(levels - 2, -1, -1):
    if scores[level] >= scores[level + 1]:
        ans += scores[level] - scores[level + 1] + 1
        scores[level] = scores[level + 1] - 1
print(ans)