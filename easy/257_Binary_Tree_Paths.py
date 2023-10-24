class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None
        if (not root.left) and (not root.right):
            return [str(root.val)]
        ReturnList = []
        if root.left:
            ReturnList = ReturnList + self.binaryTreePaths(root.left)
        if root.right:
            ReturnList = ReturnList + self.binaryTreePaths(root.right)
        for i in range(len(ReturnList)):
            ReturnList[i] = str(root.val) + '->' + ReturnList[i]
        return ReturnList
