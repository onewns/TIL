import sys
import bisect
sys.stdin = open('../input.txt', 'r')
"""
1. 이진탐색을 직접 구현한 풀이(solution1)
2. bisect 라이브러리를 이용한 풀이(solution2)
3. 딕셔너리의 in 연산을 사용한 풀이(solution3)

1,2는 성능적인 부분에서 큰 차이가 없었으며
3의 경우 1, 2에 비해 조금더 빨랐지만 메모리 사용 측면에서 단점이 있음
"""


# 직접 구현한 이진 탐색
def binary_search(nums, goal):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == goal:
            return True
        elif nums[mid] < goal:
            left = mid + 1
        else:
            right = mid - 1
    return False


# 직접 구현한 이진 탐색을 이용한 풀이
def solution1(n, m, nums, targets):
    answer = []
    nums.sort()
    for target in targets:
        if binary_search(nums, target):
            answer.append('1')
            continue
        answer.append('0')
    return '\n'.join(answer)


# bisect 라이브러리를 이용한 풀이
def solution2(n, m, nums, targets):
    answer = []
    nums.sort()
    for target in targets:
        if target == nums[bisect.bisect(nums, target) - 1]:
            answer.append('1')
            continue
        answer.append('0')
    return '\n'.join(answer)


# dictionary 의 in 연산을 이용한 풀이
def solution3(n, m, nums, targets):
    answer = []
    nums_dict = {num: True for num in nums}
    for target in targets:
        if target in nums_dict:
            answer.append('1')
            continue
        answer.append('0')
    return '\n'.join(answer)


N = int(input())
arr1 = sorted(list(map(int, input().split())))
M = int(input())
arr2 = list(map(int, input().split()))
print(solution1(N, M, arr1, arr2))
print(solution2(N, M, arr1, arr2))
print(solution3(N, M, arr1, arr2))
