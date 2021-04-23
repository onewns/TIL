import sys
sys.stdin = open('../input.txt', 'r')
"""
시작 오후 3:22
끝 오후 3: 54

풀이방법
1. 집, 치킨집 좌표 추출 => houses, chickens 라는 배열에 (row_index, col_index) 형태로 저장 
2. 집, 치킨집 좌표간의 거리계산 => distance 라는 2차원 배열에 가로축을 chicken_index 로 하여 저장
3. itertools 를 이용해서 cases 만들기
4. 각각의 case 에 대해 거리를 계산
"""
from itertools import combinations


def solution(size, limit, board):

    # 좌표를 추출
    houses = []
    chickens = []
    for row_index in range(size):
        for col_index in range(size):
            if board[row_index][col_index] == 1:
                houses.append((row_index, col_index))
            elif board[row_index][col_index] == 2:
                chickens.append((row_index, col_index))

    # 집, 치킨집간의 거리 계산
    distance = [[] for _ in range(len(chickens))]
    for chicken_index in range(len(chickens)):
        chicken_row, chicken_col = chickens[chicken_index]
        for house_row, house_col in houses:
            distance[chicken_index].append(abs(chicken_row - house_row) + abs(chicken_col - house_col))

    # cases 만들기
    cases = combinations(range(len(chickens)), limit)

    # 각각의 case 검사
    answer = float('inf')
    for case in cases:
        temp = 0
        for house_index in range(len(houses)):
            temp += min([distance[chicken_index][house_index] for chicken_index in case])
        answer = min(temp, answer)
    return answer


N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
print(solution(N, M, arr))
