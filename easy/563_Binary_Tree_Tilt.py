# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ret1, ret2 = self.calcSumAndAbs(root)
        return ret2
    
    def calcSumAndAbs(self, root: TreeNode):
        if not root:
            return 0, 0
        
        if not root.left and not root.right:
            Sum = root.val
            AbsSum = 0
            root.val = 0
            return Sum, AbsSum
        
        leftSum = 0
        rightSum = 0
        leftAbsSum = 0
        rightAbsSum = 0
        if root.left:
            leftSum ,leftAbsSum = self.calcSumAndAbs(root.left)
        if root.right:
            rightSum ,rightAbsSum = self.calcSumAndAbs(root.right)
        Sum = leftSum + rightSum + root.val
        AbsSum = abs(leftSum - rightSum)
        root.val = AbsSum
        return Sum, AbsSum + leftAbsSum + rightAbsSum