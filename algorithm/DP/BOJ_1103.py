import sys
sys.stdin = open('../input.txt', 'r')
"""
시작 오후 3:31
끝 오후 9:22

dp 를 만들어 놓고 쓰지 않아서 계속 시간초과

"""


def dfs(y, x, dp, board, visited):
    if not (0 <= y < len(board) and 0 <= x < len(board[0])) or board[y][x] == 'H':
        return 0
    if visited[y][x]:
        return -1
    if dp[y][x]:
        return dp[y][x]
    visited[y][x] = 1
    distance = int(board[y][x])
    for ny, nx in [(y, x + distance), (y, x - distance), (y + distance, x), (y - distance, x)]:
        temp = dfs(ny, nx, dp, board, visited)
        if temp >= 0:
            dp[y][x] = max(dp[y][x], temp + 1)
        else:
            dp[y][x] = -1
            return -1
    visited[y][x] = 0
    return dp[y][x]


def solution(row, col, board):
    dp = [[0] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    dfs(0, 0, dp, board, visited)
    return dp[0][0]


N, M = map(int, input().split())
arr = list(list(input()) for _ in range(N))
print(solution(N, M, arr))
