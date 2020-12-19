import sys
sys.stdin = open("../input.txt", 'r')


def cal(n1, operator, n2):
    if operator == '+':
        return [n1 + n2]
    elif operator == '*':
        return [n1 * n2]
    else:
        return [n1 - n2]


def make_case(now, end, case):
    case = case[:]
    if now >= end:
        cases.append(list(reversed(case)))
        return
    make_case(now + 1, end, case)  # 괄호 추가 위치가 아니면  바로 그 다음으로 넘어감
    case.append(now * 2)  # 괄호를 추가했다면
    make_case(now + 2, end, case)  # 바로 다음에는 갈수가 없으므로 다음다음으로 이동


n = int(input())
expression = list(map(lambda x: int(x) if x.isdigit() else x, input()))  # 숫자는 int로 연산자는 str그대로
cases = []
make_case(0, n // 2, [])
ans = -float('inf')
for c in cases:
    changed_expression = expression[:]
    for i in c:
        changed_expression[i:i + 3] = cal(expression[i], expression[i + 1], expression[i + 2])
    while len(changed_expression) > 1:
        changed_expression[0:3] = cal(changed_expression[0], changed_expression[1], changed_expression[2])
    ans = max(ans, changed_expression[0])
print(ans)