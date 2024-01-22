# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        count_list = self.countMode(root)
        counted = Counter(count_list).most_common()
        
        max_count = counted[0][1]
        
        ret = []
        for i in counted:
            if i[1] == max_count:
                ret.append(i[0])
            else:
                break
        return ret
        
        
        
    def countMode(self, root: TreeNode) -> List[int]:
        retList = []
        retList.append(root.val)
        if root.left:
            retList += self.countMode(root.left)
        if root.right:
            retList += self.countMode(root.right)
        return retList