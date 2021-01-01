import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
cards = list(map(lambda x: (int(x), True), input().split()))
cards = dict(cards)
m = int(input())
ans = []
for c in list(map(int, input().split())):
    if c in cards:
        ans.append(1)
        continue
    ans.append(0)
print(*ans)