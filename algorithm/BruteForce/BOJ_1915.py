import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def solution(n, m, board):
    size = 0
    for row in range(n):
        if n - row <= size:
            return size ** 2

        for col in range(m):
            if m - col <= size:
                break

            if board[row][col]:
                temp = 1
                while True:
                    if row + temp < n and col + temp < m and board[row + temp][col + temp]:
                        for i in range(temp):
                            if not (board[row + temp][col + i] and board[row + i][col + temp]):
                                break
                        else:
                            temp += 1
                            continue
                    break
                size = max(size, temp)

    return size ** 2


N, M = map(int, input().split())
arr = [list(map(int, input().replace('\n', ''))) for _ in range(N)]
print(solution(N, M, arr))
