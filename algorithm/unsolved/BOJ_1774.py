import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


n, m = map(int, input().split())
positions = {i: tuple(map(int, input().split())) for i in range(1, n+1)}
print(positions)
adj = {i: [] for i in range(1, n+1)}
for _ in range(m):
    g1, g2 = map(int, input().split())
    adj[g1].append(g2)
    adj[g2].append(g1)
print(adj)
unions = []
