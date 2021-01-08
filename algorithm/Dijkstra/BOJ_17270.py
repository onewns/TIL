import sys
sys.stdin = open('../input.txt', 'r')
import heapq


def dijkstra(dist, start):
    hq = []  # 초기 heapq
    dist[start] = 0  # 시작지점 시간 0으로
    heapq.heappush(hq, (dist[start], start))  # heapq 에 시작점 삽입
    while hq:
        cur_time, cur_node = heapq.heappop(hq)
        for next_node, time in adj[cur_node]:  # 다음 노드및 시간 탐색
            if cur_time + time < dist[next_node]:  # 더 빠르게 갈 수 있으면
                dist[next_node] = cur_time + time  # 최신화
                heapq.heappush(hq, (dist[next_node], next_node))


v, e = map(int, input().split())
adj = {i: [] for i in range(1, v+1)}
for _ in range(e):
    start_node, end_node, weight = map(int, input().split())
    adj[start_node].append((end_node, weight))
    adj[end_node].append((start_node, weight))  # 양방향이므로
jh, sh = map(int, input().split())
INF = float('inf')
j_dist = [INF for _ in range(v+1)]  # 배열 초기 상탵
s_dist = [INF for _ in range(v+1)]
dijkstra(j_dist, jh)  # dijkstra를 통한 dist배열 업데이트
dijkstra(s_dist, sh)
mintime = INF  # 최소시간 변수
for node in range(1, v+1):  # 최소시간 탐색
    if j_dist[node] and s_dist[node]:
        mintime = min(mintime, j_dist[node] + s_dist[node])
candidate = []  # 후보군
for node in range(1, v+1):
    if node == jh or node == sh:  # 출발지면 안됨
        continue
    # 최소시간이고 j가 먼저 도착하면
    if j_dist[node] + s_dist[node] == mintime and j_dist[node] <= s_dist[node]:
        # 후보군에 삽입 hq 이유 => j가 빠르게 도착하면 최소시간 및 번호가 작은 노드
        heapq.heappush(candidate, (j_dist[node], node))  # 첫번째거리로 두번째 노드 번호로
try:
    t, ans = heapq.heappop(candidate)
    print(ans)
except IndexError:  # 불가능할때
    print(-1)
