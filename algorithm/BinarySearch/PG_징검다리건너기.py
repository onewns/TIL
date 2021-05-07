"""
시작 오후 2:48
끝 오후 3:44
"""


def check(stones, k, mid):
    now = 0
    for stone in stones:
        if stone < mid:
            now += 1
            if now == k:
                return False
            continue
        now = 0
    return True


def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)
    while left <= right:
        mid = (left + right) // 2
        if check(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


print(solution([1,1,1,1, 2, 4, 5, 3, 2, 1, 4, 2, 5, 1,1,1,1,1,1,1,1,1,1,1,1], 3))
