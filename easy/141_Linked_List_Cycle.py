class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        checklist = []
        while not head==None:
            if head in checklist:
                return True
            else:
                checklist.append(head)
                head = head.next
        return False