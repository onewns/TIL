class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # my style 32ms 15.5MB
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev

        # use recursion 36ms 20MB
        def reverse(node, prev=None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)