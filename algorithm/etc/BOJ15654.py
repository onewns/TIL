import sys
sys.stdin = open('../input.txt', 'r')


def perm(now, end, array, candidate):
    if len(array) == end:
        a = " ".join(array)
        plist.append(a)
        return
    if now == n:
        return
    for i in range(n):
        if not candidate[i]:
            array.append(arr[i])
            candidate[i] = True
            perm(now + 1, end, array, candidate)
            array.pop()
            candidate[i] = False


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr = list(map(str, arr))
plist = []
perm(0, m, [], [False for _ in range(n)])
print(*plist, sep="\n")