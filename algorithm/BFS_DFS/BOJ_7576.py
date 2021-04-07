import sys
sys.stdin = open('../input.txt', 'r')


"""
오후 9:36
bfs
"""
from collections import deque


def solution(x_size, y_size, board):
    answer = 0
    q = deque()
    for y in range(y_size):
        for x in range(x_size):
            if board[y][x] == 1:
                q.append((y, x))
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        y, x = q.popleft()
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < y_size and 0 <= nx < x_size and not board[ny][nx]:
                board[ny][nx] = board[y][x] + 1
                q.append((ny, nx))
    for idy in range(y_size):
        for idx in range(x_size):
            if not board[idy][idx]:
                return -1
            answer = max(answer, board[idy][idx])
    return answer - 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, arr))
