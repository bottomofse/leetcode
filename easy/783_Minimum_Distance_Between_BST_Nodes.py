# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        data_list = []
        def dfs(node, data_list):
            if node.left:
                dfs(node.left, data_list)
            data_list.append(node.val)
            if node.right:
                dfs(node.right, data_list)
        dfs(root, data_list)
        minimum = float('inf')
        for i in range(len(data_list) - 1):
            minimum = min(minimum, data_list[i + 1] - data_list[i])
        return minimum




