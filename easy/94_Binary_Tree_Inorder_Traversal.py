class Solution:    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        returnList = []
        if root.left != None:
            returnList += self.inorderTraversal(root.left)
        returnList += [root.val]
        if root.right != None:
            returnList += self.inorderTraversal(root.right)
        return returnList
