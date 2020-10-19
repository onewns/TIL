class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        # my style (new ListNode) 24ms 14.2MB
        ans = h = ListNode()while head:
        if head.next:
            n1 = head.val
            head = head.next
            n2 = head.val
            head =head.next
            h.next = ListNode(n2)
            h = h.next
            h.next = ListNode(n1)
            h = h.next
        else:
            n1 = head.val
            head = head.next
            h.next = ListNode(n1)
        # return ans.next

        # swap value 32ms 14MB
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        # return head

        # use loop 24ms 14.2MB
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        # return root.next

        # use recursion 32ms 14.1MB
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        # return head