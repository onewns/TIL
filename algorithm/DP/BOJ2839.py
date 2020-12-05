import sys
sys.stdin = open('../input.txt', 'r')


def dp(weight):
    memo = [0, 0, 0, 1, 0, 1]  # 메모 array
    if weight == 4:  # 예외 처리
        return -1
    elif weight == 3:  # 예외 처리
        return 1
    else:
        now = 5   # 현재 숫자
        while now != weight:  # 타겟이 될 때 까지
            now += 1  # 숫자 1씩 추가
            if memo[now - 3] == 0 and memo[now - 5] == 0:  # 현재 숫자가 가능확인
                memo.append(0)  # 안되니까 0
            elif memo[now - 3] and memo[now - 5]:  # 2가지 경로가 가능한 상황
                memo.append(min(memo[now - 3], memo[now -5]) + 1)  # 둘중에 작은거로 선탯
            else:  # 둘중에 1가지 경로만 가능한 상황
                memo.append(max(memo[now - 3], memo[now -5]) + 1)  # 0이면 안되므로 max로 처리
        if memo[weight]:  # while 문이 다 돈후에 타겟 숫자가 가능한지 확인
            return memo[weight]  # 가능하다면 memo에서 가져오기
        else:
            return -1


print(dp(int(input())))
