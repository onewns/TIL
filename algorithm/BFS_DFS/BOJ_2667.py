import sys
sys.stdin = open('../input.txt', 'r')

"""
stack 을 이용한 dfs

(0, 0) 부터 순서대로 방문하며 0이 아니면 단지 갯수를 증가시키고
dfs 를 시작 => 단지의 크기를 구해서 배열에 담아 놓기
단지 갯수와 단지의 크기를 출력
"""


def dfs(y, x, matrix, visited):
    answer = 1
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stack = [(y, x)]
    visited[y][x] = 1
    while stack:
        r, c = stack.pop()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(visited) and 0 <= nc < len(visited) and matrix[nr][nc] and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                answer += 1
    return answer


def solution(size, board):
    visited = [[0] * size for _ in range(size)]
    answer = []
    for r in range(size):
        for c in range(size):
            if board[r][c] and not visited[r][c]:
                answer.append(dfs(r, c, board, visited))
            visited[r][c] = 1
    answer.sort()
    print(len(answer))
    print(*answer, sep='\n')
    return


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
solution(n, arr)
