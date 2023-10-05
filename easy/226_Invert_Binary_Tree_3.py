class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        L, R = root.left, root.right
        root.left = self.invertTree(R)        
        root.right = self.invertTree(L)
        return root
