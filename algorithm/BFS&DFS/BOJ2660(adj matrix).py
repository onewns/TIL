import sys
sys.stdin = open("../input.txt", 'r')


from collections import deque


def bfs(people, matrix):
    point = people  # 최소 점수를 찾기 위한 변수 선언
    visited = [[0 for _ in range(people + 1)] for _ in range(people + 1)]  # 방문표시 0번 인덱스는 점수 표시
    for person in range(1, people + 1):  # 사람들 순서대로 검사
        q = deque()
        q.append((person, 0))  # 초기 노드
        temp = point  # 사람별 임시 점수 변수
        while q:
            now, depth = q.popleft()  # queue 에서 뽑아와서
            if not visited[person][now]:  # 해당 노드를 방문하지 않았다면
                visited[person][now] = True  # 방문표시를 하고
                temp = depth  # 임시 점수를 최신화
                for next_person in range(1, people + 1):  # 다음 노드를 탐색
                    if matrix[now][next_person]:  # 가능한 경로가 있다면
                        q.append((next_person, depth + 1))  # 큐에 추가
        visited[person][0] = temp  # while 문이  visited에 점수 저장
    candidate = []  # 후보자 list
    for c in range(1, people + 1):  # 후보자 탐색
        if visited[c][0] < point:  # 기존 점수 보다 낮다면
            point = visited[c][0]  # 점수를 최신화 하고
            candidate = [c]  # 후보자를 최신화
        elif visited[c][0] == point:  # 기존 점수와 같다면
            candidate.append(c)  # 후보자 추가
    print(point, len(candidate))
    print(*candidate)


n = int(input())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
p1, p2 = 0, 0
while p1 != -1:
    p1, p2 = map(int, input().split())
    arr[p1][p2] = 1
    arr[p2][p1] = 1
bfs(n, arr)