import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def solution(w, n, nums):
    sums = {}
    nums.sort()
    min3 = nums[0] + nums[1] + nums[2]
    nums = list(filter(lambda x: x <= w - min3, nums))
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if w - nums[i] - nums[j] in sums:
                return "YES"

        for j in range(i):
            sums[nums[i] + nums[j]] = True

    return 'NO'


W, N = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(W, N, arr))
