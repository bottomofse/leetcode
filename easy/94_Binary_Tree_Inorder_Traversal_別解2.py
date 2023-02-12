from collections import deque
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def search(node):
            if node is None:
                return deque([])
            return search(node.left) + deque([node.val]) + search(node.right)
        return list(search(root))