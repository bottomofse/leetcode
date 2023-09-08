class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        returnList = []
        if not root:
            return returnList
        if root.left:
            returnList += self.postorderTraversal(root.left)
        if root.right:
            returnList += self.postorderTraversal(root.right)
        return returnList + [root.val]
