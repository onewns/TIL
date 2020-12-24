import sys
sys.stdin = open("../input.txt", 'r')


def safe(y, x):
    if 0 <= y < 8 and 0 <= x < 8:
        return True


while True:
    try:
        line = list(input().split('/'))
        board = [list('-' for _ in range(8)) for _ in range(8)]
        P, p, n, b, r, q, k = 'P', 'p', 'n', 'b', 'r', 'q', 'k'
        moves = {
            '-': [],
            P: [(-1, -1), (-1, 1)],
            p: [(1, -1), (1, 1)],
            n: [(1, -2), (1, 2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)],
            b: [(-1, -1), (-1, 1), (1, -1), (1, 1)],
            r: [(1, 0), (-1, 0), (0, 1), (0, -1)],
            q: [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)],
            k: [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)],
        }
        visited = [list(0 for _ in range(8)) for _ in range(8)]
        for y in range(8):
            idx = 0
            for status in line[y]:
                if status.isdigit():
                    idx += int(status)
                else:
                    if status == P:
                        board[y][idx] = status
                    else:
                        board[y][idx] = status.lower()
                    visited[y][idx] = 1
                    idx += 1
        for idy in range(8):
            for idx in range(8):
                if board[idy][idx] in [P, p, n, k]:
                    for dy, dx in moves[board[idy][idx]]:
                        ny, nx = idy + dy, idx + dx
                        if safe(ny, nx) and board[ny][nx] == '-':
                            visited[ny][nx] = 1
                else:
                    for dy, dx in moves[board[idy][idx]]:
                        ny, nx = idy + dy, idx + dx
                        while safe(ny, nx) and board[ny][nx] == '-':
                            visited[ny][nx] = 1
                            ny += dy
                            nx += dx
        # print(*visited, sep='\n')
        print(sum(visited, []).count(0))
    except EOFError:
        break


