import sys
sys.stdin = open('../input.txt', 'r')


n, m = map(int, input().split())
strings = set()
for _ in range(n):
    strings.add(input())
ans = 0
for _ in range(m):
    if input() in strings:
        ans += 1
print(ans)