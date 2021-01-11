import sys
sys.stdin = open('../input.txt', 'r')


# 에로토스테네스 => 느림
n = int(input())
prime_candi = [1 for _ in range(n + 1)]
for num in range(2, n + 1):
    if prime_candi[num]:
        while not n % num:
            print(num)
            n //= num
        if n == 1:
            break
        for k in range(num * 2, n + 1, num):
            prime_candi[k] = 0

# 에라토스테네스x 훨씬 빠름
n = int(input())
while not n % 2:
    print(2)
    n //= 2
while n != 1:
    for i in range(3, n + 1, 2):
        while not n % i:
            print(i)
            n //= i
        if n == 1:
            break
