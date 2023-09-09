class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A_list = []
        while headA:
            A_list.append(headA)
            headA = headA.next        
        B_list = []
        while headB:
            B_list.append(headB)
            headB = headB.next
        common = []
        while A_list and B_list:
            A = A_list.pop()
            B = B_list.pop()
            if A == B:
                common.append(A)
            else:
                break
        if common:
            return common[-1]
        else:
            return None