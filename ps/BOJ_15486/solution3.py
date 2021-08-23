import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


def brute_force(today, day, temp, table):
    if today >= day:
        return temp
    time, money = table[today]
    temp1 = temp
    if today + time <= day:
        temp1 += money
    return max(
        brute_force(today + time, day, temp1, table),
        brute_force(today + 1, day, temp, table)
    )


def solution(day, table):
    return brute_force(0, day, 0, table)


if __name__ == '__main__':
    n = int(input())
    arr = list(tuple(map(int, input().split())) for _ in range(n))
    print(solution(n, arr))
