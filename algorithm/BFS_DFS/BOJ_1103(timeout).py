import sys
sys.stdin = open('../input.txt', 'r')
"""
시작 오후 4:47
끝 오후 6:28 시간초과

"""


def solution(row, col, board):
    adj = [[[] for _ in range(col)] for _ in range(row)]
    for row_index in range(row):
        for col_index in range(col):
            jump = board[row_index][col_index]
            if jump:
                if 0 <= row_index - jump < row and board[row_index - jump][col_index]:
                    adj[row_index][col_index].append((row_index - jump, col_index))
                if 0 <= row_index + jump < row and board[row_index + jump][col_index]:
                    adj[row_index][col_index].append((row_index + jump, col_index))
                if 0 <= col_index - jump < col and board[row_index][col_index - jump]:
                    adj[row_index][col_index].append((row_index, col_index - jump))
                if 0 <= col_index + jump < col and board[row_index][col_index + jump]:
                    adj[row_index][col_index].append((row_index, col_index + jump))
    visited = [[0] * col for _ in range(row)]
    stack = [(0, 0, 1)]
    path = []
    answer = 0
    while stack:
        row_index, col_index, depth = stack.pop()
        if visited[row_index][col_index]:
            return -1
        visited[row_index][col_index] = 1
        path.append((row_index, col_index, board[row_index][col_index], depth))
        if adj[row_index][col_index]:
            for r, c in adj[row_index][col_index]:
                stack.append((r, c, depth + 1))
        else:
            answer = max(answer, len(path))
            r, c, cnt, d = path.pop()
            visited[r][c] = 0
            while stack and d != stack[-1][2]:
                r, c, cnt, d = path.pop()
                visited[r][c] = 0
            visited[r][c] = 0
    return answer


N, M = map(int, input().split())
arr = list(list(map(lambda x: int(x) if x.isdigit() else 0, list(input()))) for _ in range(N))
print(solution(N, M, arr))
