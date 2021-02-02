import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline
import heapq


students = {}
hq = []
n, m = map(int, input().split())
for i in range(m):
    s = input()[:8]
    students[s] = i
for s_num, order in students.items():
    heapq.heappush(hq, (order, s_num))
cnt = 0
n = min(n, len(hq))
while cnt < n:
    print(heapq.heappop(hq)[1])
    cnt += 1
