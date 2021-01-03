import sys
sys.stdin = open('../input.txt', 'r')


def immigration_time(start, end):
    ans = (start + end) // 2
    left, right = start, end
    while left <= right:
        mid = (left + right) // 2
        possible_person = 0  # mid 시간에 심사 받는 사람수
        for time in times:
            possible_person += (mid // time)
        if possible_person < person:  # 심사를 다 못받으면
            left = mid + 1  # 시간을 늘림
        else:  # 다 받으면
            ans = mid
            right = mid - 1  # 시간을 줄임
    return ans


n, person = map(int, input().split())
times = [int(input()) for _ in range(n)]
print(immigration_time(1, max(times) * person // n + 1))