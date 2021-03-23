import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


def dfs(node):
    dfs_print = [node]
    stack = [node]
    dfs_visited[node] = 1
    while stack:
        cur = stack.pop()
        if not dfs_visited[cur]:
            dfs_print.append(cur)
            dfs_visited[cur] = 1
        for mid in reversed(adj[cur]):
            if not dfs_visited[mid]:
                stack.append(mid)
    print(*dfs_print)


def bfs(node):
    bfs_print = [node]
    q = deque([node])
    bfs_visited[node] = 1
    while q:
        cur = q.popleft()
        for mid in adj[cur]:
            if not bfs_visited[mid]:
                bfs_print.append(mid)
                bfs_visited[mid] = 1
                q.append(mid)
    print(*bfs_print)


n, m, v = map(int, input().split())
adj = {i: [] for i in range(1, n + 1)}
dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)
for _ in range(m):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
for i in range(1, n + 1):
    adj[i].sort()
dfs(v)
bfs(v)
