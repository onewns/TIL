import sys
sys.stdin = open("../input.txt", 'r')


def re_combination(depth, arr, temp):
    if depth == m:
        p_list.append(' '.join(temp))
        return
    for i in range(len(arr)):
        temp.append(arr[i])
        re_combination(depth + 1, arr[i:], temp)
        temp.pop()


n, m = map(int, input().split())
nums = list(map(str, sorted(list(map(int, input().split())))))
p_list = []
re_combination(0, nums, [])
print(*p_list, sep="\n")
