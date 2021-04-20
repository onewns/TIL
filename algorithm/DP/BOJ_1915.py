import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


"""
board가 가로 세로 커져 감에 따른 dp
"""


def solution(n, m, board):
    answer = 0
    dp = list([board[r][c] if r * c == 0 else 0 for c in range(m)] for r in range(n))
    for row in range(1, n):
        for col in range(1, m):
            if board[row][col]:
                dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
    for r in range(n):
        answer = max(answer, *dp[r])
    return answer ** 2


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
print(solution(N, M, arr))
