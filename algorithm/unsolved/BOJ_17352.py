import sys
sys.stdin = open('../input.txt', 'r')

"""
분리집합으로 풀어보기
"""

n = int(input())
adj = {i: [] for i in range(1, n+1)}
for _ in range(n-2):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
visited = [0] * (n + 1)
stack = [1]
visited[1] = 1
while stack:
    start = stack.pop()
    for mid in adj[start]:
        if not visited[mid]:
            visited[mid] = 1
            stack.append(mid)
for i in range(1, n+1):
    if not visited[i]:
        print(1, i)
        break
