# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maximum, sum_ = self.searchSumandMax(root)
        return sum_
        
    def searchSumandMax(self, root: TreeNode):
        if not root:
            return 0,0
        if not root.left and not root.right:
            return 0,0
        left_max, left_sum = self.searchSumandMax(root.left)
        right_max, right_sum = self.searchSumandMax(root.right)
        if root.left:
            left_max += 1
        if root.right:
            right_max += 1
        return max(left_max, right_max), max(left_sum, right_sum, left_max + right_max)