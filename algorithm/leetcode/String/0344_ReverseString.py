#leetcode 344
def reverseString(self, s: List[str]) -> None:

# my_style 192ms, 18.6MB
    for i in range(len(s)//2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

# two pointer 204ms, 18.5MB
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[left], s[right]
        left += 1
        right -= 1

# use reverse 200ms, 18.3MB
    s.reverse()