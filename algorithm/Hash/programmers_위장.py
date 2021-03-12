def solution(clothes):
    closet = {}
    for name, part in clothes:
        if part not in closet:
            closet[part] = 1
        closet[part] += 1
    answer = 1
    for num in closet.values():
        answer *= num
    answer -= 1
    return answer