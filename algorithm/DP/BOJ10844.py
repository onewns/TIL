import sys
sys.stdin = open('../input.txt', 'r')


def stairs_num(n):  # 끝자리 숫자가 어떻게 끝나는지가 중요
    arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # n = 1 일때 초기 세팅
    for _ in range(n-1):  # 원하는 단계 만큼 반복
        # 끝자리가 0, 9 인경우 전단계의 1, 8 을 그대로 가져옴
        # 아닐 경우 전 단계의 양 옆의 수의 개수의 합을 가져옴
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9] = \
            arr[1] % 1000000000, (arr[0] + arr[2]) % 1000000000, (arr[1] + arr[3]) % 1000000000,\
            (arr[2] + arr[4]) % 1000000000, (arr[3] + arr[5]) % 1000000000, (arr[4] + arr[6]) % 1000000000,\
            (arr[5] + arr[7]) % 1000000000, (arr[6] + arr[8]) % 1000000000, (arr[7] + arr[9]) % 1000000000,\
            arr[8] % 1000000000
    return sum(arr) % 1000000000


print(stairs_num(int(input())))