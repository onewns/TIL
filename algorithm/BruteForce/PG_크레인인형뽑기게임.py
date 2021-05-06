"""
시작 오후 5:45
끝 오후 5: 56
"""


def solution(board, moves):
    answer = 0
    bucket = []
    moves = list(map(lambda x: x - 1, moves))
    for move in moves:
        for depth in range(len(board)):
            if board[depth][move]:
                if bucket and bucket[-1] == board[depth][move]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[depth][move])
                board[depth][move] = 0
                break

    return answer


input_board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
input_moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(input_board, input_moves))
