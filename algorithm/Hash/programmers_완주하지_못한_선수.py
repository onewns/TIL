def solution(participant, completion):
    name_dic = {}
    for name in completion:
        if name in name_dic:
            name_dic[name] += 1
        else:
            name_dic[name] = 1
    for name in participant:
        if name not in name_dic or name_dic[name] == 0:
            return name
        name_dic[name] -= 1

a = hash('asdf')
print(a)
