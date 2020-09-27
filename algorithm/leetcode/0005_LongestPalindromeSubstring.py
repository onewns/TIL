# leetcode 5

def longestPalindrome(self, s: str) -> str:

    # my style 3276ms 14.3MB
    length = len(s)
    while 1:
        for start in range(len(s) - length + 1):
            temp = s[start:start+length]
            if temp == temp[::-1]:
                return temp
        length -= 1

    # use two pointer 248ms 14.2MB
    def expand(left,right):
        while left >= 0 and right <= len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right-1]
    if len(s) < 2 or s == s[::-1]:
        return s
    result = ""
    for i in range(len(s)-1):
        result = max(result, expand(i,i+1), expand(i,i+2), key=len)
    return result