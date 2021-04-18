import sys
sys.stdin = open('../input.txt', 'r')

"""
O(n^3 log n)
"""

def binary_search(start, end, target):
    left, right = start, end
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            left = mid + 1
        else:
            right = mid - 1


def is_possible():
    for n1_idx in range(n-3):
        if nums[n1_idx] >= limit:
            continue
        for n2_idx in range(n1_idx+1, n-2):
            if nums[n1_idx] + nums[n2_idx] >= limit:
                continue
            for n3_idx in range(n2_idx+1, n-1):
                if nums[n1_idx] + nums[n2_idx] + nums[n3_idx] >= limit:
                    continue
                if binary_search(n3_idx+1, n-1, limit - (nums[n1_idx] + nums[n2_idx] + nums[n3_idx])):
                    return "YES"
    return 'NO'


limit, n = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)
print(is_possible())