import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque

start, target = map(int, input().split())
q = deque([start])
visited = [0] * 100001
visited[start] = 1
while q:
    now = q.popleft()
    if now == target:
        print(visited[target] - 1)
        break
    if 0 <= now - 1 <= 100000 and not visited[now - 1]:
        visited[now - 1] = visited[now] + 1
        q.append(now - 1)
    if 0 <= now + 1 <= 100000 and not visited[now + 1]:
        visited[now + 1] = visited[now] + 1
        q.append(now + 1)
    if 0 <= now * 2 <= 100000 and not visited[now * 2]:
        visited[now * 2] = visited[now] + 1
        q.append(now * 2)
