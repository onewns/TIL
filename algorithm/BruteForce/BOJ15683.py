import sys
sys.stdin = open("../input.txt", 'r')


def is_safe(y, x):  # 인덱스 검사하기 위한 함수
    if 0 <= y < size_y and 0 <= x < size_x:
        return True
    return False


def dfs(now, end, matrix):
    global ans
    if now == end:  # 종료 시점
        ans = min(ans, sum(matrix, []).count(0))
        return
    cctv, y, x = cctvs[now]
    for possible in possibles[cctv]:  # 감시 가능한 방향 목록
        temp_matrix = [list(matrix[y][x] for x in range(size_x)) for y in range(size_y)]  # 체크하기 위한 2차원배열
        for di in possible:  # 가능한 방향중 1개씩 확인
            ny, nx = y, x
            while is_safe(ny, nx) and arr[ny][nx] != 6:  # 인덱스 문제가 없고 벽이 아니면
                temp_matrix[ny][nx] = 1
                ny += dy[di]
                nx += dx[di]
        dfs(now + 1, end, temp_matrix)  # 경우에 대한 방향 탐색후 다음 cctv로 이동


size_y, size_x = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(size_y)]
cctvs = []
ans = size_x * size_y  # 최대값으로 설정
dy = [-1, 0, 1, 0]  # 12시 부터 시계방향
dx = [0, 1, 0, -1]  # 12시 부터 시계방향
possibles = [[],  # cctv종류별 감시 가능 방향 표시
             [[0], [1], [2], [3]],
             [[0, 2], [1, 3]],
             [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
             [[0, 1, 2, 3]]
             ]
for idy in range(size_y):
    for idx in range(size_x):
        if arr[idy][idx]:
            if arr[idy][idx] and arr[idy][idx] != 6:
                cctvs.append((arr[idy][idx], idy, idx))
dfs(0, len(cctvs), arr)
print(ans)