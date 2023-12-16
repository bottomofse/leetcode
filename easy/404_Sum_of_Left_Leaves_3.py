class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        left = 0
        if (root.left is not None) and (root.left.left is None) and (root.left.right is None):
            left += root.left.val
        left += self.sumOfLeftLeaves(root.left)
        left += self.sumOfLeftLeaves(root.right)

        return left
