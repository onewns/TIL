"""
오후 10:23
오후 11:15

itertools 의 product 이용하면 비교적 쉽게 구현 가능
조금 느림
"""


# 처음 푼 방법 : 가장 빠름 함수 안에 함수 정의.....
def solution(user_id, banned_id):
    def comb(now, temp):
        temp = temp[:]
        if now == len(banned_id):
            temp.sort()
            if temp not in ans:
                ans.append(temp)
            return
        for b_candi in ban_dict[now]:
            if not used[b_candi]:
                used[b_candi] = True
                temp.append(b_candi)
                comb(now+1, temp)
                temp.pop()
                used[b_candi] = False

    ban_dict = [[] for _ in banned_id]
    for b_id in range(len(banned_id)):
        for u_id in user_id:
            if len(u_id) == len(banned_id[b_id]):
                for char_idx in range(len(banned_id[b_id])):
                    if banned_id[b_id][char_idx] != '*' and banned_id[b_id][char_idx] != u_id[char_idx]:
                        break
                else:
                    ban_dict[b_id].append(u_id)
    ans = []
    used = {u: False for u in user_id}
    comb(0, [])
    return len(ans)


# product 를 사용하지 않은 풀이
def combination(banned_depth, users, banned, answer, temp):
    temp = temp[:]
    if banned_depth == len(banned):
        temp.sort()
        if len(temp) == len(banned) and temp not in answer:
            answer.append(temp)
        return
    ban_user = banned[banned_depth]
    for user_index in range(len(users)):
        user = users[user_index]
        if user not in temp and len(user) == len(ban_user):
            for i in range(len(user)):
                if ban_user[i] != '*' and ban_user[i] != user[i]:
                    break
            else:
                temp.append(user)
                combination(banned_depth+1, users, banned, answer, temp)
                temp.pop()


def solution1(user_id, banned_id):
    answer = []
    combination(0, user_id, banned_id, answer, [])
    return len(answer)


# product 를 사용한 풀이
from itertools import product


def solution_product(user_id, banned_id):
    answer = set()
    candidate = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        ban = banned_id[i]
        for user in user_id:
            if len(user) == len(ban):
                for j in range(len(user)):
                    if ban[j] != '*' and ban[j] != user[j]:
                        break
                else:
                    candidate[i].append(user)
    products = map(set, product(*candidate))
    for temp in products:
        if len(temp) == len(banned_id):
            answer.add(''.join(temp))
    return len(answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
solution1(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
solution_product(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
