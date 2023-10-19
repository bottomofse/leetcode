class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        h = head
        while h:
            length += 1
            h = h.next

        if length == 1: return True
        
        h2 = head
        arr = []
        for i in range(length // 2):
            arr.append(h2.val)
            h2 = h2.next
        if length % 2 == 1: h2 = h2.next

        while arr:
            if arr.pop() != h2.val:
                return False
            h2 = h2.next
        return True