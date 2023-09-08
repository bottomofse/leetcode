class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        returnList = []
        returnList.append(root.val)
        if root.left:
            returnList += self.preorderTraversal(root.left)
        if root.right:
            returnList += self.preorderTraversal(root.right)
        return returnList
