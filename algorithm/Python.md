# Python



### BOJ 17281

```python
# 시간초과

# runners = deque()
first, second, third = 0, 0, 0
## base = [0,0,0] 이거도 시간초과
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
```

