def solution(phone_book):
    trie = {}
    for phone_num in phone_book:
        cur = trie
        for num in phone_num:
            if num not in cur:
                cur[num] = {}
            cur = cur[num]
        cur['end'] = True
    for phone_num in phone_book:
        cur = trie
        for num in phone_num:
            cur = cur[num]
        if len(cur.keys()) > 1:
            return False
    return True


def solution1(phone_book):
    phone_dict = {phone_num: True for phone_num in phone_book}
    for phone_num in phone_book:
        temp = ''
        for num in phone_num:
            temp += num
            if temp != phone_num and temp in phone_dict:
                return False
    return True
