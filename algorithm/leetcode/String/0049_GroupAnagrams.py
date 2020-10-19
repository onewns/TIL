# leetcode 49
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    # my style 88ms 16.9MB
    dic = {}
    for word in strs:
        key = "".join(sorted(list(word)))
        if key in dic:
            dic[key].append(word)
        else:
            dic[key] = [word]
    ans = [words for words in dic.values()]
    return ans
    sor
    # use defalutdict 84ms 17.4MB
    dic = collections.defaultdict(list)
    for word in strs:
        dic[''.join(sorted(word))].append(word)
    return dic.values()