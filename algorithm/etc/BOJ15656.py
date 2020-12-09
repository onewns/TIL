import sys
sys.stdin = open('../input.txt', 'r')


def re_perm(depth, temp):
    if depth == end:
        p_list.append(' '.join(temp))
        return
    for num in nums:
        temp.append(num)
        re_perm(depth + 1, temp)
        temp.pop()


n, end = map(int, input().split())
nums = list(map(str, sorted(list(map(int, input().split())))))
p_list = []
re_perm(0, [])
print(*p_list, sep="\n")