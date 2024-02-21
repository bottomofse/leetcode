# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.check = {}
    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.search(root)
        bottom = float('inf')
        sec_bottom = float('inf')
        for i in self.check:
            if i < bottom:
                if bottom != float('inf'):
                    sec_bottom = bottom
                bottom = i
                continue
            if i < sec_bottom:
                sec_bottom = i
                continue
        return sec_bottom if sec_bottom != float('inf') else -1
        
    def search(self, root):
        self.check[root.val] = 0
        if root.left is None and root.right is None:
            return
        if root.left:
            self.search(root.left)
        if root.right:
            self.search(root.right)