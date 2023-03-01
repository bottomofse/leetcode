class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        tmp, blanced = self.depthAndbalanced(root)
        return blanced
    
    #ê[Ç≥Ç∆ÅAïΩçtÇ©ÅiïΩçtÅFTrueÅjÇï‘Ç∑
    def depthAndbalanced(self, curNode: TreeNode):
        if not curNode:
            return 0, True
        left_depth, left_balanced = self.depthAndbalanced(curNode.left)
        right_depth, right_balanced = self.depthAndbalanced(curNode.right)
        if abs(left_depth - right_depth) <= 1 and left_balanced and right_balanced:
            return max(left_depth, right_depth) + 1,True
        else:
            return max(left_depth, right_depth) + 1, False