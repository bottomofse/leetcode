class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        Before = None
        Current = head
        while Current:
            if Current.val == val:
                if Current == head:
                    head = Current.next
                    Before = Current
                    Current = Current.next
                else:
                    Before.next = Current.next
                    Current = Current.next
            else:
                Before = Current
                Current = Current.next

        return head
