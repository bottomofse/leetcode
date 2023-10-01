class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_val, right_val = 0, 0
        if root.left is not None:
            left_val = self.countNodes(root.left)
        if root.right is not None:
            right_val = self.countNodes(root.right)
        return left_val + 1 + right_val
