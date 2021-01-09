import sys
sys.stdin = open('../input.txt', 'r')


def quick_sort(start, end):
    global flag
    if start < end:
        left, right = start, end
        pivot = (left + right) // 2
        while left < right:
            while arr[left] < arr[pivot] and left < right:
                left += 1
            while arr[right] >= arr[pivot] and left < right:
                right -= 1
            if left < right:
                if left == pivot:
                    pivot = right
                arr[left], arr[right] = arr[right], arr[left]
        arr[pivot], arr[right] = arr[right], arr[pivot]
        pivot = right
        quick_sort(start, pivot - 1)
        quick_sort(pivot + 1, end)


import random
flag = True
while flag:
    arr = random.sample(range(1, 30), 10)
    # arr = [5, 14, 20, 4, 22, 11, 27, 16, 23, 17]
    print(arr)
    quick_sort(0, len(arr) - 1)
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            print(False)
            flag = False
            break
