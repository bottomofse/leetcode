class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tmpLeft = root.left
        tmpRight = root.right
        if tmpLeft:
            root.right = self.invertTree(tmpLeft) 
        if tmpRight:
            root.left = self.invertTree(tmpRight)
        if not tmpLeft:
            root.right = None
        if not tmpRight:
            root.left = None
        
        return root
