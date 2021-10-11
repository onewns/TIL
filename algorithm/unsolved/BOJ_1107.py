import sys
sys.stdin = open('../input.txt', 'r')


def num(temp, depth):
    global over, less
    if depth == len(target) + 1:
        temp = int(temp)
        if temp >= int(target):
            over = min(over, temp)
        if temp <= int(target):
            less = max(less, temp)
        return
    for p in possible:
        num(temp + str(p), depth+1)
        num('0' + temp, depth+1)


target = input()
n = int(input())
if n == 10:
    t = int(''.join(list(map(str, target))))
    print(abs(t - 100))
else:
    if n:
        disabled = list(map(int, input().split()))
        possible = [i for i in range(10) if i not in disabled]
    else:
        possible = list(range(10))
    over = float('inf')
    less = -float('inf')
    num('', 0)
    answer = min(
        abs(over - int(target)) + len(str(over)),
        abs(less - int(target)) + len(str(less)),
        abs(100 - int(target))
    )
    print(over, less)
    print(answer)