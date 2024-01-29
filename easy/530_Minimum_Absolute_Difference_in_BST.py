# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        all_node_val_list = self.createTreeList(root)
        all_node_val_list.sort()
        #print(all_node_val_list)
        minimum = 10000000
        for i in range(len(all_node_val_list) - 1):
            minimum = min(minimum, abs(all_node_val_list[i + 1] - all_node_val_list[i]))
        return minimum
            
            
        
        
    def createTreeList(self, root: TreeNode) -> List[int]:
        ret = [root.val]
        if root.left:
            ret += self.createTreeList(root.left)
        if root.right:
            ret += self.createTreeList(root.right)
        return ret
