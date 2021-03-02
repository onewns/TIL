import sys
sys.stdin = open('../input.txt', 'r')
import heapq


city_num = int(input())
between = list(map(int, input().split()))
goal = sum(between)
costs = list(map(int, input().split()))
hq = [(costs[0], 0)]
for i in range(len(between) - 1):
    hq.append((costs[i + 1], hq[i][1] + between[i]))
heapq.heapify(hq)
answer = 0
while hq:
    cost, position = heapq.heappop(hq)
    if position < goal:
        answer += (goal - position) * cost
        goal = position
        if goal == 0:
            break
print(answer)