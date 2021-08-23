def score_to_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 50:
        return 'D'
    return 'F'


def swap_row_col(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


def check_highest(arr, value):
    if max(arr) == value and arr.count(value) == 1:
        return False
    return True


def check_lowest(arr, value):
    if min(arr) == value and arr.count(value) == 1:
        return False
    return True


def check_score(arr, value):
    if check_highest(arr, value) and check_lowest(arr, value):
        return True
    return False


def solution(scores):
    answer = ''
    swap_row_col(scores)
    for student_index in range(len(scores)):
        student_score = scores[student_index]
        if not check_score(student_score, student_score[student_index]):
            student_score.remove(student_score[student_index])
        answer += score_to_grade(sum(student_score) / len(student_score))
    return answer
