import sys
sys.stdin = open("../input.txt", 'r')


from collections import deque


def bfs(n):
    visited = [False for _ in range(people + 1)]  # 노드 방문 표시
    visited[0], visited[n] = True, True  # 시작하는 노드와 0번 노드는 방문
    q = deque([(n, 0)])  # 출발점 queue에 삽입
    depth = 0  # 얼마나 뻗어 나가야 하는지
    while q:
        v, temp = q.popleft()  # 노드를 가져와서
        if not visited[v]:  # 방문하지 않았으면
            visited[v] = True  # 방문표시를 하고
            depth = temp  # depth 를 최신화
        for nv in adj[v]:  # 인접리스트를 이용해서 다음 노드 탐색
            if not visited[nv]:  # 방문하지 않은  노드 발견시
                q.append((nv, temp+1))  # queue에 해당 노드를 저장
    return n, depth


people = int(input())
adj = {i: [] for i in range(1, people + 1)}
while True:
    p1, p2 = map(int, input().split())
    if p1 == -1:
        break
    adj[p1].append(p2)  # 인접리스트 생성
    adj[p2].append(p1)  # 양방향 이므로 두쪽다
candidate = []
p = 100
for i in range(1, people+1):
    person, d = bfs(i)  # 후보와 depth를 가져옴
    if d > p:  # depth가 현재 최저점보다 크면
        continue  # 의미가 없음
    if d < p:  # dpeth가 현재 최저점보다 작으면
        p = d  # 최저점을 최신화
        candidate = [person]  # 후보를 최신화
    else:  # depth가 현재 최저점과 같으면
        candidate.append(person)  # 후보를 추가

print(p, len(candidate))
print(*candidate)