class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ret_sum = 0
        if root.left and not root.left.left and not root.left.right:
            ret_sum += root.left.val
        if root.left:
            ret_sum += self.sumOfLeftLeaves(root.left)
        if root.right:
            ret_sum += self.sumOfLeftLeaves(root.right)
        return ret_sum
