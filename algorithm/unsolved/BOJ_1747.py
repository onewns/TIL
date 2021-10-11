import sys
sys.stdin = open('../input.txt', 'r')


def make_pal(depth, temp, end):
    if depth == end:
        return
    if temp and temp[0] in ['1', '3', '5', '7', '9']:
        pals.append(temp + temp[::-1])
        for i in range(10):
            pals.append(temp + str(i) + temp[::-1])
    for i in range(10):
        make_pal(depth + 1, temp + str(i), end)


def is_prime(num):
    d = 3
    while d < num:
        if not num % d:
            return False
        d += 2
    return True


n = int(input())
pals = ['3', '5', '7']
make_pal(0, '', len(str(n)) // 2 + 2)
pals.sort(key=lambda x: len(x))
if n < 3:
    print(2)
else:
    for pal in pals:
        pal = int(pal)
        if pal >= n and is_prime(pal):
            print(pal)
            break
