# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ret = []
        self.average(ret, [root])
        return ret
    
    def average(self, result, nodes):
        if not nodes:
            return
        next_nodes = []
        sum_val = 0
        for i in nodes:
            sum_val += i.val
            if i.left:
                next_nodes.append(i.left)
            if i.right:
                next_nodes.append(i.right)
        result.append(sum_val / len(nodes))
        self.average(result, next_nodes)