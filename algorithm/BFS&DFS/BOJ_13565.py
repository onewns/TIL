import sys
sys.stdin = open('../input.txt', 'r')


def is_safe(y, x):
    if 0 <= y < size_y and 0 <= x < size_x:
        return True


def dfs():
    stack = [(0, x) for x in range(size_x) if not visited[0][x]]
    while stack:
        y, x = stack.pop()
        visited[y][x] = 2
        if y == size_y - 1:
            return True
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if is_safe(ny, nx) and not visited[ny][nx]:
                stack.append((ny, nx))


size_y, size_x = map(int, input().split())
visited = [list(map(int, input())) for _ in range(size_y)]
direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
if dfs():
    print('YES')
else:
    print('NO')