import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
lefts, rights = [], []
for _ in range(n):
    start, destination = map(int, input().split())
    if start > destination:
        lefts.append(destination)
        rights.append(start)
if lefts:
    ans = m + (max(rights) - min(lefts)) * 2
else:
    ans = m
print(ans)
