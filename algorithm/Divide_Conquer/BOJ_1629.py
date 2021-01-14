import sys
sys.stdin = open('../input.txt', 'r')


a, b, c = map(int, input().split())
memo = [a]
now = 2
while now <= b:
    memo.append(memo[-1] ** 2 % c)
    now *= 2
b = bin(b)[-1:1:-1]
ans = 1
for i in range(len(b)):
    if b[i] == '1':
        ans *= memo[i]
print(ans % c)
