import sys
sys.stdin = open("../input.txt", 'r')


"""
1 2 3 4
상하좌우
matrix에 [상어번호, 냄새지속시간]
shaek_locations = {상어번호: 위치 정보, 방향정보}
상어가 이동가능
이동시 방향을 고려해야 함
1. 냄새지속시간이 0 인경우
2. 냄새지속시간이 0은 아니지만 상어번호가 자기랑 같은 경우
이동이 완료된후
matrix에 상어번호가 2개 이상 있으면 해당 상어 내쫓고 위치 정보에서 삭제
상어가 존재하는 상황이면
냄새지속시간이 1이면 0으로 바꾸고 상어 정보 삭제
2~4면 1씩 감소
0이면 4로 바꿈
shark_locations이 1개가 남을때 까지 반복
"""


def safe(y, x):
    if 0 <= y < size and 0 <= x < size:
        return True


size, shark_population, duration = map(int, input().split())
# 상어의 위치정보를 담을 딕셔너리 (key = 상어번호, value = 위치정보, 방향정보
shark_location = {i: [] for i in range(1, shark_population + 1)}
matrix = [list(map(lambda x: [[int(x)], duration] if int(x) else [[], 0], input().split())) for _ in range(size)]
for idy in range(size):
    for idx in range(size):
        if matrix[idy][idx][0]:
            shark_location[matrix[idy][idx][0][0]] = [idy, idx]
init_directions = list(map(int, input().split()))
for init_direction_idx in range(shark_population):
    shark_location[init_direction_idx + 1].append(init_directions[init_direction_idx])
# 상어의 방향에 따른 우선순위 방향을 담을 딕셔너리
shark_priority = {shark_num: {d: [] for d in range(1, 5)} for shark_num in range(1, shark_population + 1)}
for shark_n in range(1, shark_population + 1):
    for d in range(1, 5):
        shark_priority[shark_n][d] = list(map(int, input().split()))
# 1, 2, 3, 4 = 각각 상하좌우
directions = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
time = 0
while shark_population > 1:
    for shark_num, shark_data in shark_location.items():  # 상어의 위치정보를 가져와서 움직이기 시작
        shark_y, shark_x, shark_direction = shark_data[0], shark_data[1], shark_data[2]
        # 빈칸이 있는지 탐색
        for di in shark_priority[shark_num][shark_direction]:  # 우선순위 순서로 탐색
            dy, dx = directions[di]
            ny, nx = shark_y + dy, shark_x + dx
            if safe(ny, nx) and not matrix[ny][nx][1]:  # 빈칸이 있다면
                matrix[ny][nx][0].append(shark_num)  # 상어를 해당 칸에 집어 넣어 놓고
                shark_location[shark_num] = [ny, nx, di]  # 상어의 위치, 방향정보 최신화
                break  # 종료
        else:  # 주위에 빈칸이 없을때 실행
            for di in shark_priority[shark_num][shark_direction]:
                dy, dx = directions[di]
                ny, nx = shark_y + dy, shark_x + dx
                if safe(ny, nx) and matrix[ny][nx][0][0] == shark_num:  # 자신의 냄새라면
                    shark_location[shark_num] = [ny, nx, di]  # 상어의 위치, 방향 정보 최신화
                    break
    for idy in range(size):
        for idx in range(size):
            if matrix[idy][idx][1]:
                matrix[idy][idx][1] -= 1  # 냄새를 1개씩 줄여줌
                if not matrix[idy][idx][1]:  # 냄새가 없어지면
                    matrix[idy][idx][0] = []  # 해당칸의 상어 정보 초기화
            while len(matrix[idy][idx][0]) > 1:  # 한칸에 2마리 이상의 상어가 있으면
                delete_shark_num = matrix[idy][idx][0].pop()  # 삭제할 상어 선택
                del(shark_location[delete_shark_num])  # 상어 삭제
                shark_population -= 1  # 상어수 감소
    for shark_num, shark_data in shark_location.items():  # 상어의 위치 정보를 기반으로
        shark_y, shark_x = shark_data[0], shark_data[1]
        matrix[shark_y][shark_x][0] = [shark_num]  # 냄새가 1남았을때 0이 되며 상어의 정보가 사라지는 것을 방지
        matrix[shark_y][shark_x][1] = duration  # 지속시간 초기화
    time += 1  # 시간 지남
    if time > 1000:  # 1000이 넘으면
        print(-1)  # 불가능
        break
else:  # 정상적으로 종료 되면
    print(time)  # 시간출력
