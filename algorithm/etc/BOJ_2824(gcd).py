import sys
sys.stdin = open('../input.txt', 'r')


def gcd(n1, n2):
    while n1 % n2:
        n1, n2 = n2, n1 % n2
    return n2


a = int(input())
a_nums = list(map(int, input().split()))
b = int(input())
b_nums = list(map(int, input().split()))
idx = 0
ans = a_num = b_num = 1
for na in a_nums:
    a_num *= na
for nb in b_nums:
    b_num *= nb
answer = str(gcd(a_num, b_num))
if len(answer) >= 10:
    print(answer[len(answer)-9:])
else:
    print(answer)
