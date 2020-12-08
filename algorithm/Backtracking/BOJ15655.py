import sys
sys.stdin = open('../input.txt', 'r')


def combination(depth, length, arr):
    if len(arr) == length:
        plist.append(' '.join(arr))
        return
    if len(arr) + n - depth < length:
        return
    arr.append(nums[depth])
    combination(depth + 1, length, arr)
    arr.pop()
    combination(depth + 1, length, arr)


n, m = map(int, input().split())
nums = list(map(str, sorted(list(map(int, input().split())))))
plist = []
combination(0, m, [])
print(*plist, sep='\n')
