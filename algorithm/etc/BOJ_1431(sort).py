import sys
sys.stdin = open('../input.txt', 'r')


def sum_nums(string):
    s = 0
    for char in string:
        if char.isdigit():
            s += int(char)
    return s


n = int(input())
serials = [input() for _ in range(n)]
serials.sort(key=lambda serial: (len(serial), sum_nums(serial), serial))
print(*serials, sep='\n')
