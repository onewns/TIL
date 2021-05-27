import sys
sys.stdin = open('../input.txt', 'r')

"""
오후 6:26
오후 6:44
"""


def dfs(size, board):
    visited = [[0] * size for _ in range(size)]
    stack = [(0, 0)]
    while stack:
        y, x = stack.pop()
        if y == size - 1 and x == size -1:
            return True
        visited[y][x] = 1
        for ny, nx in [(y + board[y][x], x), (y, x + board[y][x])]:
            if 0 <= ny < size and 0 <= nx < size and not visited[ny][nx]:
                stack.append((ny, nx))
    return False


def solution(size, board):
    if dfs(size, board):
        return 'HaruHaru'
    return 'Hing'


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))
