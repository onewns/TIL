import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def bfs(node):
    q = deque()
    q.append(node)
    count = 0
    while q:
        cur = q.popleft()
        visited[cur] = True
        count += 1
        for next_node in adj[cur]:
            if not counts[next_node]:
                q.append(next_node)
    return count


computer_num, link_num = map(int, input().split())
adj = {start: [] for start in range(1, computer_num + 1)}
for _ in range(link_num):
    end, start = map(int, input().split())
    adj[start].append(end)
counts = [0] * (computer_num + 1)
for s in range(1, computer_num + 1):
    counts[s] = bfs(s)
max_num = max(counts)
answer = []
for index, val in enumerate(counts):
    if val == max_num:
        answer.append(index)
print(*answer)