"""
오후 6:12
오후 8:00

후위 표기법 변환법
※ 연산기호를 stack 에서 처리할 때
현재 연산 기호보다 우선순위가 높거나 !!같은!! 경우를 모두 pop 시킨후 stack 에 추가해야 함!!
"""


# 중위 표기법을 후위 표기법으로 변환하는 함수
def change(expression, order):
    changed_expression = []
    operator = []
    for word in expression:
        if word in order:
            if operator:
                while operator and order[operator[-1]] >= order[word]:
                    changed_expression.append(operator.pop())
                operator.append(word)
            else:
                operator.append(word)
        else:
            changed_expression.append(word)
    while operator:
        changed_expression.append(operator.pop())
    return changed_expression


# 후위 표기법으로 표현된 식을 계산하는 함수
def calculator(expression):
    stack = []
    for word in expression:
        if word in ['-', '+', '*']:
            n2 = stack.pop()
            n1 = stack.pop()
            if word == '-':
                stack.append(n1 - n2)
            elif word == '+':
                stack.append(n1 + n2)
            else:
                stack.append(n1 * n2)
        else:
            stack.append(word)
    answer = stack[0]
    return abs(answer)


def solution(expression):
    answer = 0
    new_expression = []
    num = ''
    for char in expression:
        if char.isdigit():
            num += char
        else:
            new_expression.append(int(num))
            new_expression.append(char)
            num = ''
    new_expression.append(int(num))
    cases = [
        {'+': 0, '-': 1, '*': 2},
        {'+': 0, '-': 2, '*': 1},
        {'+': 1, '-': 0, '*': 2},
        {'+': 1, '-': 2, '*': 0},
        {'+': 2, '-': 0, '*': 1},
        {'+': 2, '-': 1, '*': 0}
    ]

    for case in cases:
        changed_expression = change(new_expression, case)
        print(changed_expression)
        answer = max(calculator(changed_expression), answer)
    return answer


print(solution("100-200*300-500+20"))