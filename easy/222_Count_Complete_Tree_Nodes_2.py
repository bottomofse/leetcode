class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)
