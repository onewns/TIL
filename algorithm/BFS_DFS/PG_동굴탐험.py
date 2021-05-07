"""
오후 3:44
오후 4:20
"""
from collections import deque


def solution(n, path, order):
    # dic = {next_node: prev_node for prev_node, next_node in order}
    dic = {prev_node: next_node for prev_node, next_node in order}

    requires = set(dic.keys())
    impossibles = set(dic.values())

    visited = [0 for _ in range(n)]

    adj = [[] for _ in range(n)]
    for n1, n2 in path:
        adj[n1].append(n2)
        adj[n2].append(n1)

    if 0 in impossibles:
        return False
    q = deque()

    if 0 in requires:
        impossibles.remove(dic[0])
        del dic[0]
    q.append(0)
    visited[0] = 1

    not_black = set()
    while q:
        node = q.popleft()
        for next_node in adj[node]:
            if next_node in impossibles:
                not_black.add(next_node)
            elif not visited[next_node]:
                q.append(next_node)
                visited[next_node] = 1
                if next_node in requires:
                    impossibles.remove(dic[next_node])
                    if dic[next_node] in not_black:
                        q.append(dic[next_node])
                    del dic[next_node]
    if len(dic):
        return False
    return True
