import sys
sys.stdin = open('../input.txt', 'r')


def gcd(n1, n2):
    while n1 % n2:
        n1, n2 = n2, n1 % n2
    return n2


g, l = map(int, input().split())
m = l // g
for a in range(round(m**0.5), 0, -1):
    if not m % a and gcd(a, m // a) == 1:
        print(a * g, m // a * g)
        break
