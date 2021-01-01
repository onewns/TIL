import sys
sys.stdin = open('../input.txt', 'r')


def binary_search(start, end):
    ans = 0
    while start <= end:
        dist = (start + end) // 2
        prev_house = houses[0]
        cnt = 1
        for house_idx in range(1, house_num):
            if houses[house_idx] >= dist + prev_house:
                cnt += 1
                prev_house = houses[house_idx]
        if cnt >= c:
            ans = dist
            start = dist + 1
        else:
            end = dist - 1
    return ans


house_num, c = map(int, input().split())
houses = sorted(list(int(input()) for _ in range(house_num)))
print(binary_search(1, houses[-1] - houses[0]))
