import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def pa_length(left, right):
    pa_len = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        chicken = 0
        for pa in pas:
            chicken += pa // mid
        if chicken >= chicken_num:
            pa_len = mid
            left = mid + 1
        else:
            right = mid - 1
    ans = sum(pas) - pa_len * chicken_num
    print(ans)


pa_num, chicken_num = map(int, input().split())
pas = [int(input()) for _ in range(pa_num)]
pa_length(1, max(pas))
