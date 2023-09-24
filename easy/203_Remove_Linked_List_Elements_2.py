class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = head
        while new_head and new_head.val == val:
            new_head = new_head.next
        if new_head is None : return new_head

        bef, cur, aft = None, new_head, new_head.next
        while cur:
            if cur.val == val:
                bef.next = aft
                cur = aft
                aft = aft.next if aft is not None else None
            else:
                bef = cur
                cur = aft
                aft = aft.next if aft is not None else None
        return new_head
