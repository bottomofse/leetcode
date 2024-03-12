"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        data = []
        self.search(root, data)
        return data

    def search(self, node: 'Node', tree_list: List[int]):
        if not node:
            return
        for i in node.children:
            self.search(i, tree_list)
        tree_list.append(node.val)