from heapq import heappush, heappop


def solution(N, road, K):
    answer = 0
    INF = float('inf')
    dist = [INF for _ in range(N + 1)]
    dist[1] = 0
    adj = {i: {} for i in range(1, N + 1)}
    for start, end, cost in road:
        if end not in adj[start] or start not in adj[end]:
            adj[start][end] = cost
            adj[end][start] = cost
        else:
            adj[start][end] = min(adj[start][end], cost)
            adj[end][start] = min(adj[end][start], cost)
    hq = []
    for mid, cost in adj[1].items():
        heappush(hq, (cost, mid))

    while hq:
        

    return answer
