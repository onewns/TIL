#leetcode 125

# my_style 268ms, 14.9MB
strr = list(input().lower())
for c in range(len(strr)-1,-1,-1):
    if not strr[c].isalnum():
        del strr[c]

for i in range(len(strr)//2):
    if strr[i] != strr[len(strr) - 1 - i]:
        print("false")
        break
else:
    print("true")

# use deque 44ms, 19.2MB
import collections
def isPalindrome(self, s:str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

# use slicing 29ms , 15.6MB
def isPalindrome(self, s:str) -> bool:
    s = s.lower()
    #정규식
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]