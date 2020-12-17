import sys
sys.stdin = open('../input.txt', 'r')


def binary_search(target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return 0


n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))
p_list = []
for t in targets:
    p_list.append(binary_search(t))
print(*p_list, sep='\n')