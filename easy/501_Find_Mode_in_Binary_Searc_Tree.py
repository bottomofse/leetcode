# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        val_dic = {}
        node_list = [root]
        while node_list:
            next_node_list = []
            for t_node in node_list:
                if t_node.val in val_dic:
                    val_dic[t_node.val] += 1
                else:
                    val_dic[t_node.val] = 1
                if t_node.left:
                    next_node_list.append(t_node.left)
                if t_node.right:
                    next_node_list.append(t_node.right)
            node_list = next_node_list
        
        max_mode = -1
        for i in val_dic:
            max_mode = max(max_mode, val_dic[i])
            
        ret = []
        for i in val_dic:
            if val_dic[i] == max_mode:
                ret.append(i)
        
        return ret
