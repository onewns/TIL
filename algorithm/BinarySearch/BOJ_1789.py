import sys
sys.stdin = open('../input.txt', 'r')


def howmany(left, right):
    ans = 1  # 숫자는 최소 1개
    while left <= right:
        mid = (left + right) // 2  # mid == 숫자가 몇개 인지
        if mid * (mid + 1) // 2 == n:  # 1부터 mid까지 합친것과 n이 같으면 바로 return
            return mid
        elif mid * (mid + 1) // 2 > n:  # 1 부터 mid까지 합친게 n보다 크면
            right = mid - 1  # 탐색범위를 왼쪽으로 좁혀야함
        else:  # 조건에 적합하므로
            left = mid + 1  # 탐색범위를 오른쪽으로 재조정 하고
            ans = mid  # 이후 탐색에서 답이 없을수도 있으니 답을 최신화
    return ans


n = int(input())
print(howmany(1, n))