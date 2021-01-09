import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def quick_sort_recursion(a, start, end):
    left, right = start, end
    if left < right:
        pivot = (left + right) // 2
        while left < right:
            while a[left] < a[pivot] and left < right:
                left += 1
            while a[right] >= a[pivot] and left < right:
                right -= 1
            if left < right:
                a[left], a[right] = a[right], a[left]
                if left == pivot:
                    pivot = right
        a[right], a[pivot] = a[pivot], a[right]
        pivot = right
        quick_sort_recursion(a, start, pivot - 1)
        quick_sort_recursion(a, pivot + 1, end)


def quick_sort_loop(a, start, end):
    stack = [(start, end)]
    while stack:
        start, end = stack.pop()
        left, right = start, end
        if left < right:
            pivot = (left + right) // 2
            while left < right:
                while a[left] < a[pivot] and left < right:
                    left += 1
                while a[right] >= a[pivot] and left < right:
                    right -= 1
                if left < right:
                    a[left], a[right] = a[right], a[left]
                    if left == pivot:
                        pivot = right
            a[right], a[pivot] = a[pivot], a[right]
            pivot = right
            stack.append((start, pivot - 1))
            stack.append((pivot + 1, end))


n = int(input())
arr = [int(input()) for _ in range(n)]
quick_sort_recursion(arr, 0, len(arr) - 1)
quick_sort_loop(arr, 0, len(arr) - 1)
print(*arr, sep='\n')
