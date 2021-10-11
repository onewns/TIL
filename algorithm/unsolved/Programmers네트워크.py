"""
오후 5:40
오후 6:05
"""


from collections import deque


def bfs(n, computers, visited):
    q = deque([n])
    visited[n] = 1
    while q:
        v = q.popleft()
        for k in range(len(computers)):
            if computers[v][k] and not visited[k]:
                visited[k] = 1
                q.append(k)
    return visited


def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited = bfs(i, computers, visited)
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
