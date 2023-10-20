class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward = []
        while head:
            forward.append(head.val)
            head = head.next
        return forward == forward[::-1]
