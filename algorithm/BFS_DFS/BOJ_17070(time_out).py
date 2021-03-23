import sys
sys.stdin = open('../input.txt', 'r')


def is_safe(y, x, next_s):
    for dy, dx in check[next_s]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < size and 0 <= nx < size and not matrix[ny][nx]:
            continue
        else:
            return False
    return True


def move_pipe(y, x, s):
    global ans
    if y == size - 1 and x == size - 1:
        ans += 1
        return
    for next_s in state[s]:
        if is_safe(y, x, next_s):
            if next_s == 0:
                move_pipe(y, x + 1, next_s)
            elif next_s == 1:
                move_pipe(y + 1, x, next_s)
            else:
                move_pipe(y + 1, x + 1, next_s)


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
# 0 == 가로, 1 == 세로, 2 == 대각선 상태
state = [
    [0, 2],  # 각 상태별 검사해야 하는 다음 상태
    [1, 2],
    [0, 1, 2]
]
check = [[(0, 1)], [(1, 0)], [(1, 0), (0, 1), (1, 1)]]
ans = 0
move_pipe(0, 1, 0)
print(ans)