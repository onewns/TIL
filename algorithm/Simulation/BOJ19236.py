import sys
sys.stdin = open("../input.txt", 'r')


def is_safe(fish_y, fish_x, shark_y, shark_x):  # 물고기가 움직일 수 있는지 확인
    if 0 <= fish_y < 4 and 0 <= fish_x < 4 and not (fish_y == shark_y and fish_x == shark_x):
        return True


def fish_move(fish_map):
    global ans
    positions = [0 for _ in range(17)]  # 물고기별로 위치를 저장 (상어 = 0)
    matrix = [list([] for _ in range(4)) for _ in range(4)]  # 복사 뜰 판
    for idy in range(4):  # 복사 시작
        for idx in range(4):
            if fish_map[idy][idx]:
                positions[fish_map[idy][idx][0]] = (idy, idx)
            matrix[idy][idx] = fish_map[idy][idx][:]
    shark_y, shark_x = positions[0]
    for fish_num in range(1, 17):  # 물고기 별로 움직이기 시작 (상어 제외)
        if positions[fish_num]:  # 물고기의 위치 정보가 있다면 == 물고기가 아직 먹히기 전이라면
            fish_y, fish_x = positions[fish_num]
            di = matrix[fish_y][fish_x][1]
            for _ in range(8):  # 8방향 탐색
                dy, dx = directions[di]
                ny, nx = fish_y + dy, fish_x + dx
                if is_safe(ny, nx, shark_y, shark_x):  # 갈수 있는지 검사
                    if matrix[ny][nx]:  # 가려고 하는 자리에 다른 물고기가 있으면
                        another = matrix[ny][nx][0]  # 다른 물고기의 숫자
                        matrix[fish_y][fish_x][1] = di  # 변경된 방향
                        #  물고기의 위치 정보와 맵에 표시된 정보를 최신화
                        positions[fish_num], positions[another] = positions[another], positions[fish_num]
                        matrix[ny][nx], matrix[fish_y][fish_x] = matrix[fish_y][fish_x], matrix[ny][nx]
                    else:  # 가려고 하는 자리에 물고기가 없으면
                        matrix[fish_y][fish_x][1] = di
                        #  정보 최신화
                        positions[fish_num] = (ny, nx)
                        matrix[ny][nx], matrix[fish_y][fish_x] = matrix[fish_y][fish_x], matrix[ny][nx]
                    break
                di = (di + 1) % 8  # 방향 탐색을 위해 1씩 증가
    feeds = []  # 먹을 수 있는 먹이 목록
    shark_di = matrix[shark_y][shark_x][1]  # 상어의 방향 정보
    shark_dy, shark_dx = directions[shark_di]  # 상어의 이동 방향
    shark_ny, shark_nx = shark_y + shark_dy, shark_x + shark_dx  # 상어의 새로운 위치
    while 0 <= shark_ny < 4 and 0 <= shark_nx < 4:  # 맵의 경계 까지 탐색
        if matrix[shark_ny][shark_nx]:  # 물고기가 있으면
            feeds.append(matrix[shark_ny][shark_nx][0])  # 물고기를 먹이 목록에 추가
        shark_ny += shark_dy  # 다음칸 탐색
        shark_nx += shark_dx  # 다음칸 탐색
    if feeds:  # 먹이가 있으면
        matrix[shark_y][shark_x] = []  # 현재 상어위치 비우고
        for feed in feeds:
            feed_y, feed_x = positions[feed]
            matrix[feed_y][feed_x][0] = 0  # 먹이의 위치로 상어가 이동
            fish_move(matrix)  # 재귀 실행
            matrix[feed_y][feed_x][0] = feed  # 다음번 먹이 먹는 경우를 위해 초기화
    else:  # 먹을 수 있는 먹이가 없으면 ans 와 비교후 큰값으로 교체
        t = 0
        for fish in range(1, 17):
            if not positions[fish]:
                t += fish
        ans = max(ans, t)


arr = [list([0, 0] for _ in range(4)) for _ in range(4)]
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
ans = 0
for y in range(4):
    line = list(map(int, input().split()))
    for x in range(8):
        if x & 1:
            arr[y][x // 2][1] = line[x] - 1
        else:
            arr[y][x // 2][0] = line[x]
arr[0][0][0] = 0
fish_move(arr)
print(ans)
