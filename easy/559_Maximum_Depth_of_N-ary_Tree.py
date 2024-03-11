"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        max_depth = 0
        for i in root.children:
            max_depth = max(max_depth, self.maxDepth(i))
        return 1 + max_depth