import sys
sys.stdin = open("../input.txt", 'r')
# n이 커지면 remove를 쓴 것 보다 훨씬 빠름 n^2 인것은 같으나 상수항이 다른듯


def thanos(arr):
    num = arr
    one, zero = num.count(1)//2, num.count(0)//2
    i = 0
    while one:
        if num[i]:
            del num[i]
            one -= 1
        else:
            i += 1
    i = len(num) - 1
    while zero:
        if not num[i]:
            del num[i]
            zero -= 1
        i -= 1
    return num


nums = list(map(int, input()))
print(*thanos(nums),sep='')
