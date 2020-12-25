import sys
sys.stdin = open("../input.txt", 'r')


def safe(y, x):  # 인덱스 검사 함수
    if 0 <= y < size and 0 <= x < size:
        return True
    return False


def break_wall():  # 연합만드는 함수 (dfs (stack))
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    unions = []
    visited = [list(0 for _ in range(size)) for _ in range(size)]
    for idy in range(size):
        for idx in range(size):
            stack = []
            union = []  # 연합의 좌표, 인구를 담아놓을 배열, unions의 하위 배열
            if not visited[idy][idx]:  # 방문하지 않은 좌표에 도달하면 연합찾기 시작
                stack.append((idy, idx))  # 현재 점을 넣어 놓고
                total_population = 0  # 인구를 0으로 초기화
                while stack:  # dfs 시작
                    y, x = stack.pop()  # 가장 최근 좌표를 꺼내와서
                    if not visited[y][x]:  # 방문하지 않았다면
                        visited[y][x] = 1  # 방문표시
                        union.append((y, x))  # 연합에 포함
                        total_population += matrix[y][x]  # 인구 증가
                    for i in range(4):  # 4방향 탐색
                        ny, nx = y + dy[i], x + dx[i]
                        # 방문하지 않았고 차이가 적당하다면
                        if safe(ny, nx) and not visited[ny][nx] and min_difference <= abs(matrix[ny][nx] - matrix[y][x]) <= max_difference:
                            stack.append((ny, nx))  # 스택에 추가
                if len(union) > 1:  # 연합을 요소가 1개 밖에 없는경우 필요 x
                    union.append(total_population // len(union))
                    unions.append(union)
    return unions


def population_movement():
    cnt = 0
    unions = break_wall()  # 최초 연합을 구하고
    while unions:  # 연합이 1개라도 존재하는 동안에
        for union in unions:  # 각각의 연합에 대해서
            p = union.pop()
            for idy, idx in union:
                matrix[idy][idx] = p  # 각각의 좌표에 해당 값을 계산된 인구수로 변환
        cnt += 1
        unions = break_wall()  # 다시 연합을 생성
    return cnt


size, min_difference, max_difference = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(size)]
print(population_movement())