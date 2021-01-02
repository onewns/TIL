import sys
sys.stdin = open('../input.txt', 'r')


def budget_decision(minimum, maximum):
    left, right = minimum, maximum - 1  # 예산 검색 범위
    ans = 0  # 특정값을 찾는것이 아닐경우에는 변수가 필요
    while left <= right:
        temp = (left + right) // 2  # 중간값
        temp_total = 0  # 초과하는지 검사를 위한 변수
        for budget in budgets:
            if budget <= temp:
                temp_total += budget
            else:
                temp_total += temp
        if temp_total == total_limit:  # 딱 맞다면 더이상 진행필요 x
            return temp
        elif temp_total < total_limit:  # 예산이 남는 경우 탐색범위를 오른쪽으로
            left = temp + 1
            ans = temp  # 조건에 맞기 때문에 최대예산 업데이트
        else:  # 예산이 부족하므로 탐색범위를 왼쪽으로
            right = temp - 1
    return ans


n = int(input())
budgets = sorted(list(map(int, input().split())))
total_limit = int(input())
max_budget = budgets[-1]
if sum(budgets) > total_limit:
    max_budget = budget_decision(0, max_budget)
print(max_budget)
