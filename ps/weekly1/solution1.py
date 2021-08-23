def solution(price, money, count):
    need = count * (count + 1) * price / 2
    answer = min(money - need, 0)
    return answer
