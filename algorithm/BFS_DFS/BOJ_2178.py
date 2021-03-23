import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


def is_safe(r, c):
    if 0 <= r < row_size and 0 <= c < col_size:
        return True
    return False


def bfs():
    q = deque([(0, 0)])
    while q:
        row, col = q.popleft()
        for dr, dc in di:
            nr, nc = row + dr, col + dc
            if is_safe(nr, nc) and visited[nr][nc] == 1:
                visited[nr][nc] = visited[row][col] + 1
                q.append((nr, nc))


row_size, col_size = map(int, input().split())
visited = [list(map(int, input())) for _ in range(row_size)]
di = [(-1, 0), (1, 0), (0, 1), (0, -1)]
bfs()
print(visited[-1][-1])
