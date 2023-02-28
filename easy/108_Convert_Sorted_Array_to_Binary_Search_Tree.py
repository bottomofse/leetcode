class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.makeTree(nums)
        
    def makeTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 2:
            return TreeNode(nums[1], left=TreeNode(nums[0]))
        middle = len(nums) // 2
        curNode = TreeNode(nums[middle])
        curNode.left = self.makeTree(nums[0:middle])
        curNode.right = self.makeTree(nums[middle + 1:])
        return curNode