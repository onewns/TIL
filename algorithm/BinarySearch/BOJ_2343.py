import sys
sys.stdin = open('../input.txt', 'r')


def cd_time(left, right):
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        cd_num = 1  # 현재 cd 숫자
        cd_t = mid  # 현재 cd에 남은 시간
        for time in times:
            if cd_t < time:  # 남은 시간이 레슨 영상보다 크면
                cd_num += 1  # 다음 cd로 넘어가서
                cd_t = mid - time  # 해당 레슨 시간만큼 차감
                continue
            cd_t -= time  # cd시간 차감
        if cd_num <= cd_limit:  # cd 수 여유가 있으면
            right = mid - 1  # 시간을 줄이고
            ans = mid  # 최신화
        else:  # cd 수가 모자르면
            left = mid + 1  # cd시간을 늘림
    return ans


lesson_num, cd_limit = map(int, input().split())
times = list(map(int, input().split()))
print(cd_time(max(times), max(times)*lesson_num))