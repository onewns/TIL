import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


def solution(n):
    q = deque()
    q.append(1)
    visited = [0] * (n + 1)
    visited[1] = -1
    while q:
        cur = q.popleft()
        if cur == n:
            path = [str(n)]
            while visited[cur] != -1:
                path.append(str(visited[cur]))
                cur = visited[cur]
            return "{}\n{}".format(len(path) - 1, ' '.join(path))

        if cur * 3 <= n and not visited[cur * 3]:
            visited[cur * 3] = cur
            q.append(cur * 3)

        if cur * 2 <= n and not visited[cur * 2]:
            visited[cur * 2] = cur
            q.append(cur * 2)

        if not visited[cur + 1]:
            visited[cur + 1] = cur
            q.append(cur + 1)

    return visited


N = int(input())
print(solution(N))
