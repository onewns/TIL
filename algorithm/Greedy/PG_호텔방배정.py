"""
오후 4:51

"""


def solution(k, room_number):
    answer = []
    nodes = {}
    for room in room_number:
        if room not in nodes:
            answer.append(room)
            nodes[room] = room + 1

        else:
            temp = [room]
            cur = room
            while True:
                next_room = nodes[cur]
                if next_room not in nodes:
                    answer.append(next_room)
                    temp.append(next_room)
                    break
                temp.append(next_room)
                cur = next_room
            for k in temp:
                nodes[k] = next_room + 1

    return answer


print(solution(10, [1, 2, 2, 2, 2, 3, 3, 3, 3, 1]))
