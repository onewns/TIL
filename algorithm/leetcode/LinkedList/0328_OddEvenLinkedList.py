# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # my style 52ms 16.8MB
    def oddEvenListMyStyle(self, head: ListNode) -> ListNode:
        flag = True
        odd = ListNode()
        even = ListNode()
        oddhead = odd
        evenhead = even
        while head:
            if flag:
                oddhead.next = ListNode(head.val)
                oddhead = oddhead.next
            else:
                evenhead.next = ListNode(head.val)
                evenhead = evenhead.next
            flag = not flag
            head = head.next
        oddhead.next = even.next
        return odd.next

    # use Loop 40ms 15.7MB
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head
