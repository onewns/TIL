import sys
sys.stdin = open("../input.txt", 'r')
# n이 커지면 deque를 쓴게 훨씬 빠름 n^2 인것은 같으나 상수항이 다른듯


def thanos(arr):
    one, zero = 0, 0
    for n in arr:
        if n:
            one += 1
            continue
        zero += 1
    for _ in range(one//2):
        arr.remove(1)
    arr = arr[::-1]
    for _ in range(zero//2):
        arr.remove(0)
    arr = arr[::-1]
    return arr


nums = list(map(int, input()))
print(*thanos(nums),sep='')
