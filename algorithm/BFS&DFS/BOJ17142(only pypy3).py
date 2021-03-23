import sys
sys.stdin = open("../input.txt", 'r')

from itertools import combinations
from collections import deque


def is_safe(y, x):  # 인덱스 에러 피하기 위한 함수
    if 0 <= y < size and 0 <= x < size:
        return True


def bfs(space, virus, matrix):
    global ans
    q = deque(virus)
    visited = [[0 for _ in range(size)] for _ in range(size)]
    temp = 0
    if not space:  # 초기에 빈공간이 없으면 ans = 0 확정
        ans = 0
        return
    while q and space:  # 종료조건(queue가 비거나 공간이 없는 경우)
        vy, vx, depth = q.popleft()  # queue에서 꺼내옴
        if not visited[vy][vx]:  # 꺼내온 좌표를 방문하지 않았다면
            visited[vy][vx] = depth  # depth로 방문표시
            temp = depth  # 발자국 찍었으므로 temp 변경
            if matrix[vy][vx] == '0':  # 빈공간을 방문한 경우
                space -= 1  # 빈공간의 수를 하나 줄여줌
            for i in range(4):  # 이동방향
                ny, nx = vy + dy[i], vx + dx[i]
                # 인덱스 에러가 나지 않고 방문위치가 벽이 아니며 아직 방문하지 않았다면
                if is_safe(ny, nx) and matrix[ny][nx] != '1' and not visited[ny][nx]:
                    q.append((ny, nx, depth + 1))  # queue에 행선지 추가
    if not space:  # while문이 끝나고 공간이 없다면
        if ans > -1:  # ans가 전체방문 가능하다고 되어있는 상태라면
            ans = min(ans, temp - 1)  # temp와 둘중 작은 값 선택
        else:  # ans가 전체방문 불가능하다면
            ans = temp - 1  # ans를 그대로 temp로 변화


size, virus_num = map(int, input().split())
arr = [list(input().split()) for _ in range(size)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
virus_locations = []
zero = 0
ans = -1
for y in range(size):
    for x in range(size):
        if arr[y][x] == '2':
            virus_locations.append((y, x, 1))
        elif arr[y][x] == '0':
            zero += 1
candidate = list(combinations(virus_locations, virus_num))
for candi in candidate:
    bfs(zero, candi, arr)
print(ans)