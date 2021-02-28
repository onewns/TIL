import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
nums = list(map(int, input().split()))
LIS = [nums.pop(0)]
for num in nums:
    if num < LIS[-1]:
        LIS.append(num)
    else:
        left, right = 0, len(LIS) - 1
        index = n
        while left <= right:
            mid = (left + right) // 2
            if LIS[mid] < num:
                index = mid
                right = mid - 1
            elif LIS[mid] > num:
                left = mid + 1
            else:
                index = mid
                break
        if index < n and LIS[index]:
            LIS[index] = num
print(len(LIS))
