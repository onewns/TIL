import sys
sys.stdin = open('17281.txt', 'r', encoding='utf-8')
from collections import deque


def swap(now, end):
    if now == end:
        temp_order = order[:]
        temp_order[0], temp_order[3] = temp_order[3], temp_order[0]
        orders.append(temp_order)
        return
    for n in range(now, end):
        order[now], order[n] = order[n], order[now]
        swap(now+1, end)
        order[now], order[n] = order[n], order[now]


ans = 0
order = [0, 1, 2, 3, 4, 5, 6, 7, 8]
orders = []
swap(1, len(order))
innings = int(input())
preds = []
for i in range(innings):
    preds.append(list(map(int, input().split())))

for order in orders:
    temp = 0
    player = 0
    for inning in range(len(preds)):
        out = 0
        # runners = deque()
        first, second, third = 0, 0, 0
        while out < 3:
            if not preds[inning][order[player]]:
                out += 1
            elif preds[inning][order[player]] == 1:
                temp += third
                first, second, third = 1, first, second
            elif preds[inning][order[player]] == 2:
                temp += (third + second)
                first, second, third = 0, 1, first
            elif preds[inning][order[player]] == 3:
                temp += (first + second + third)
                first, second, third = 0, 0, 1
            elif preds[inning][order[player]] == 4:
                temp += (1 + first + second + third)
                first, second, third = 0, 0, 0
            # else:
            #     runners = deque(map(lambda x: x + preds[inning][order[player]], runners))
            #     runners.append(preds[inning][order[player]])
            #     while runners and runners[0] > 3:
            #         runners.popleft()
            #         temp += 1
            player = (player + 1) % 9
        if ans > temp + 24*(innings-inning):
            break
    ans = max(ans, temp)
print(ans)
