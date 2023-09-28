class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        ret = stack[-1]
        while stack:
            t = stack.pop()
            t.next = stack[-1] if stack else None
        return ret
