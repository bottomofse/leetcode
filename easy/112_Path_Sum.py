class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        return self.calcSum(root, targetSum, 0)
    
    def calcSum(self, root: TreeNode, targetSum: int, curSum: int) -> bool:
        if root.left is None and root.right is None:
            return root.val + curSum == targetSum
        if root.left is None:
            return self.calcSum(root.right, targetSum, curSum + root.val)
        if root.right is None:
            return self.calcSum(root.left, targetSum, curSum + root.val)
        return (True if self.calcSum(root.right, targetSum, curSum + root.val) or
        self.calcSum(root.left, targetSum, curSum + root.val) else False)
