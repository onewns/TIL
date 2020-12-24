import sys
sys.stdin = open("../input.txt", 'r')


def safe(y, x):  # 인덱스 검사 함수
    if 0 <= y < 8 and 0 <= x < 8:
        return True


king_position, stone_position, move_num = map(
    lambda x: int(x) if x.isdigit() else (ord(x[0]) - 65, ord(x[1]) - 49),
    input().split())
ky, kx = king_position
sy, sx = stone_position
moves = [input() for _ in range(move_num)]
arr = [list(0 for _ in range(8)) for _ in range(8)]
arr[ky][kx], arr[sy][sx] = 'K', 'S'
d = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
for move in moves:
    dy, dx = d[move]
    nky, nkx = ky + dy, kx + dx
    nsy, nsx = sy + dy, sx + dx
    if safe(nky, nkx):
        if not arr[nky][nkx]:
            arr[nky][nkx], arr[ky][kx] = arr[ky][kx], arr[nky][nkx]
            ky, kx = nky, nkx
            continue
        else:
            if safe(nsy, nsx):
                """
                이렇게 한번에 처리하면 안됨
                arr[nsy][nsx], arr[sy][sx], arr[nky][nkx], arr[ky][kx] = 
                arr[sy][sx], arr[nsy][nsx], arr[ky][kx], arr[nky][nkx]
                """
                arr[nsy][nsx], arr[sy][sx] = arr[sy][sx], arr[nsy][nsx]
                arr[nky][nkx], arr[ky][kx] = arr[ky][kx], arr[nky][nkx]
                ky, kx, sy, sx = nky, nkx, nsy, nsx
print(chr(ky+65), chr(kx+49), sep='')
print(chr(sy+65), chr(sx+49), sep='')