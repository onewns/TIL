import sys
sys.stdin = open('../input.txt', 'r')


n, m = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(lambda elem: int(elem) - 1, input().split())
    for idx in range(x1, x2 + 1):
        for idy in range(y1, y2 + 1):
            arr[idy][idx] += 1
ans = 0
for y in range(100):
    for x in range(100):
        if arr[y][x] > m:
            ans += 1
print(ans)
