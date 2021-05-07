"""
오전 12:00
"""


# def solution(gems):
#     variance = len(set(gems))
#     gems_dic = {}
#     candidate = []
#     for gem_index in range(len(gems)):
#         gem = gems[gem_index]
#         gems_dic[gem] = gem_index
#         if len(gems_dic) == variance:
#             left = min(gems_dic.values())
#             if not candidate or gem_index - left < candidate[-1][1] - candidate[-1][0]:
#                 candidate.append([left + 1, gem_index + 1])
#     return candidate[-1]


def solution(gems):
    answer = [1, len(gems)]
    variance = len(set(gems))
    left, right = 0, 0
    gems_dic = {gems[0]: 1}
    while True:
        if len(gems_dic) == variance:
            if answer[1] - answer[0] > right - left:
                answer = [left + 1, right + 1]
            gems_dic[gems[left]] -= 1
            if gems_dic[gems[left]] == 0:
                del gems_dic[gems[left]]
            left += 1
            if left == len(gems):
                break
        else:
            right += 1
            if right == len(gems):
                break
            if gems[right] in gems_dic:
                gems_dic[gems[right]] += 1
            else:
                gems_dic[gems[right]] = 1
    return answer


print(solution(['DIA', 'EM', 'EM', 'RUB', 'DIA']))
