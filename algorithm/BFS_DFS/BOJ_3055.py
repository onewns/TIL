import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque
"""
시작 오후 9:21
끝 오후 10:02

평범한 bfs 문제
"""


def bfs(q, board, kind):
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    if kind == "water":
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (board[nr][nc] == 'S' or board[nr][nc] == '.'):
                    board[nr][nc] = '*'
                    q.append((nr, nc))
    else:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (board[nr][nc] == 'D' or board[nr][nc] == '.'):
                    if board[nr][nc] == 'D':
                        return True
                    board[nr][nc] = 'S'
                    q.append((nr, nc))


def solution(row, col, board):
    answer = 0
    hedgehog_q = deque()
    water_q = deque()
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'S':
                hedgehog_q.append((i, j))
            elif board[i][j] == '*':
                water_q.append((i, j))

    while hedgehog_q:
        answer += 1
        bfs(water_q, board, "water")
        if bfs(hedgehog_q, board, "hedgehog"):
            return answer
    return 'KAKTUS'


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
print(solution(N, M, arr))
