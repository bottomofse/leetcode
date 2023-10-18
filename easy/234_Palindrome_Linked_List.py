from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        queue = deque()
        while head:
            queue.append(head)
            head = head.next
        while queue:
            forward = queue.popleft()
            if not queue:
                return True
            back = queue.pop()
            if forward.val != back.val:
                return False
        return True