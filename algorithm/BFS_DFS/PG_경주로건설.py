from collections import deque


def solution(board):

    def bfs():
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[[float('inf') for _ in range(4)] for _ in range(len(board))] for _ in range(len(board))]
        visited[0][0] = [0, 0, 0, 0]
        q = deque()
        q.append((0, 0, 1))
        q.append((0, 0, 3))
        while q:
            y, x, direction = q.popleft()
            for i in range(4):
                dy, dx = delta[i]
                ny, nx = y + dy, x + dx
                if 0 <= ny < len(board) and 0 <= nx < len(board) and not board[ny][nx]:
                    if i == direction and visited[ny][nx][i] > visited[y][x][direction] + 100:
                        visited[ny][nx][i] = visited[y][x][direction] + 100
                        q.append((ny, nx, i))
                    elif visited[ny][nx][i] > visited[y][x][direction] + 600:
                        visited[ny][nx][i] = visited[y][x][direction] + 600
                        q.append((ny, nx, i))
        return min(visited[-1][-1])

    answer = bfs()
    return answer


solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])