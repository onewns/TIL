import sys
sys.stdin = open('../input.txt', 'r')


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if memo[a][b][c] == 'yet':
        if a < b < c:
            memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[a][b][c]


memo = [[[1 if a == 0 or b == 0 or c == 0 else 'yet' for c in range(21)] for b in range(21)] for a in range(21)]
while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
