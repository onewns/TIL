def gcd(a, b):
    n1, n2 = a, b
    while n1 % n2:
        n1, n2 = n2, n1 % n2
    return n2


def solution(w, h):
    answer = w * h
    count = gcd(w, h)
    new_w, new_h = w // count, h // count
    answer -= count * (new_w + new_h - 1)
    return answer
