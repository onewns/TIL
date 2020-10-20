# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __
class Solution:
    # my style 32ms 14.3MB
    def reverseBetweenMY(self, head: ListNode, m: int, n: int) -> ListNode:
        cnt = 1
        pre = ph = ListNode()
        rev = None
        while cnt < m and head:
            ph.next = ListNode(head.val)
            ph = ph.next
            head = head.next
            cnt += 1
        while m <= cnt <= n and head:
            rev, head, rev.next = head, head.next, rev
            cnt += 1
        ph.next = rev
        while ph.next:
            ph = ph.next
        ph.next = head
        return pre.next

    # use loop 24ms 14.1MB
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or n == m:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m-1):
            start = start.next
        end = start.next

        for _ in range(n-m):
            # tmp, start.next, end.next = start.next, end.next, end.next.next
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        return root.next