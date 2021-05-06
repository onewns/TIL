"""
오후 10:05
오후 10:22
"""


def solution(s):
    subsets = list(map(lambda x: sorted(x.split(',')), s[2:-2].split('},{')))
    subsets.sort(key=lambda x: len(x))
    answer = []
    for subset in subsets:
        for char in subset:
            if char not in answer:
                answer.append(char)
                break
    answer = list(map(int, answer))
    return answer


solution("{{123}}")
