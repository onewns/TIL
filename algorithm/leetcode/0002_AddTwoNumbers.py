# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # my style 68ms 14MB
        ans = head = ListNode(0)
        flag = 0
        while l1 or l2 or flag:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            flag, v = divmod(temp+flag,10)
            head.next = ListNode(v)
            head = head.next
        return ans.next

