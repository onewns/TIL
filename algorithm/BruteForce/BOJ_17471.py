import sys
sys.stdin = open('../input.txt', 'r')


from itertools import combinations


def is_possible(team, another):
    visited = [0 for _ in range(n)]
    stack = [0]  # 고정해놓은 1개 지역
    while stack:
        v = stack.pop()
        visited[v] = 1
        for next_v in adj[v]:  # 갈 수 있는 지역 탐색
            if not visited[next_v] and next_v in team:  # 방문 x 이고 현재 선거구에 포함되면
                stack.append(next_v)  # stack에 추가
    stack = [another]  # 다른 선거구
    while stack:
        v = stack.pop()
        visited[v] = 1
        for next_v in adj[v]:  # 경로탐색
            if not visited[next_v] and next_v not in team:  # 앞과 다른 선거구여야 함
                stack.append(next_v)
    if visited.count(0):  # 방문안한 지역이 있으면 안됨
        return False
    return True


n = int(input())
people = list(map(int, input().split()))
adj = {p: [] for p in range(n)}
# 인접지역을 인접리스트로 구현
for p1 in range(n):
    link = list(map(int, input().split()))
    for p2_idx in range(1, link[0] + 1):
        adj[p1].append(link[p2_idx] - 1)
cases = []
# n이 최대 10이므로 경우를 다 구하고 시작해도 1024 이때 첫번째를 미리 고정 => 512
for r in range(0, n - 1):
    temp = list(combinations(range(1, n), r))
    for t in temp:
        cases.append([0] + list(t))
total = sum(people)  # 전체 인구수
INF = float('inf')
ans = INF
for case in cases:  # 각각의 경우에 대해서
    temp = total
    p2 = 0
    for p in case:  # 차이를 구함
        temp -= people[p]
        temp -= people[p]
    temp = abs(temp)
    for k in range(1, n):  # 다른 선거구사람을 선택
        if k not in case:
            p2 = k
            break
    if temp < ans and is_possible(case, p2):  # 차이가 원래 답보다 작고 선거구 나누는게 가능하면
        ans = temp
if ans == INF:  # 불가능
    print(-1)
else:  # 가능
    print(ans)
