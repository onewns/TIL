from collections import deque
class Solution:
    def isPalindrome(self, head) -> bool:
        # my style (deque) 68ms 24MB
        dq = deque()
        while head is not None:
            dq.append(head.val)
            head = head.next
        while len(dq) > 1:
            if dq.pop() != dq.popleft():
                return False
        return True

        # use list 164ms 24MB
        arr = list()
        if not head:
            return True
        node = head
        while node is not None: # to list
            arr.append(node.val)
            node = node.next

        while len(arr) > 1: # check Palindrome
            if arr.pop(0) != arr.pop():
                return False
        return True

        # use Runner 64ms 24MB
        rev = None
        slow, fast = head
        while fast and fast.next: # 홀수 일때는 fast.next가 없음
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next # rev에 slow(현재)를 넣고 rev.next에는 rev(역순으로 지나온 길을 담는다)
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev