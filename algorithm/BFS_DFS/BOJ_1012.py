import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


"""
stack 을 이욯한 dfs
"""


def dfs(y, x, visited, board):
    stack = [(y, x)]
    visited[y][x] = 1
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while stack:
        y, x = stack.pop()
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(visited) and 0 <= nx < len(visited[0]) and board[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                stack.append((ny, nx))


def solution(r, c, positions):
    answer = 0
    board = [[0] * c for _ in range(r)]
    for y, x in positions:
        board[y][x] = 1

    visited = [[0] * c for _ in range(r)]
    for y, x in positions:
        if not visited[y][x]:
            dfs(y, x, visited, board)
            answer += 1
    return answer


tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())
    arr = []
    for _ in range(k):
        arr.append(tuple(map(int, input().split())))
    print(solution(m, n, arr))
