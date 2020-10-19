class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # my style 36ms 14.1MB
        if not l1 and not l2:
            return None
        ans = []
        while l1:
            ans.append(l1.val)
            l1 = l1.next
        while l2:
            ans.append(l2.val)
            l2 = l2.next
        ans.sort()
        l = ListNode(ans[0])
        k = l
        for i in range(1,len(ans)):
            k.next = ListNode(ans[i])
            k = k.next
        return l

        # use Recursion 40ms 14.1MB
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1