"""
시작 오후 5:56
끝 오후 6:11
"""


def solution(numbers, hand):
    answer = ''
    locations = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }
    right = (3, 2)
    left = (3, 0)
    for number in numbers:
        if number in [1, 4, 7]:
            left = locations[number]
            answer += 'L'
        elif number in [3, 6, 9]:
            right = locations[number]
            answer += 'R'
        else:
            right_distance = abs(locations[number][0] - right[0]) + abs(locations[number][1] - right[1])
            left_distance = abs(locations[number][0] - left[0]) + abs(locations[number][1] - left[1])

            if right_distance < left_distance:
                right = locations[number]
                answer += 'R'

            elif right_distance > left_distance:
                left = locations[number]
                answer += 'L'

            else:
                if hand == 'right':
                    right = locations[number]
                    answer += 'R'
                else:
                    left = locations[number]
                    answer += 'L'
    return answer


inputs = [
    [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"],
    [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]
]
for input_numbers, input_hand in inputs:
    print(solution(input_numbers, input_hand))