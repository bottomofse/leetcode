# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        check = {}
        self.search(check, root)
        for i in check:
            check[i] -= 1
            if k - i in check and check[k - i] >= 1:
                return True
            else:
                check[i] += 1
        return False
        
    def search(self, check, node):
        if node is None:
            return
        if node.val in check:
            check[node.val] += 1
        else:
            check[node.val] = 1
        if node.left:
            self.search(check, node.left)
        if node.right:
            self.search(check, node.right)