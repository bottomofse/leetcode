class Solution:
    def isLeaf(self, node):
            if node is None: return False
            if node.left is None and node.right is None:
                return True
            return False

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ret = 0
        if root is None: return 0
        
        if self.isLeaf(root.left):
            ret += root.left.val
        
        ret += self.sumOfLeftLeaves(root.left)
        ret += self.sumOfLeftLeaves(root.right)
        
        return ret
