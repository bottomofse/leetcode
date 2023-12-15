class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        #ïùóDêÊ
        nodes = [root]
        sum_val = 0
        while nodes:
            #for i in nodes:
            #    print(str(i.val) + ' : ', end='')
            #print('')
            next_nodes = []
            for node in nodes:
                if node.left and not node.left.left and not node.left.right:
                    #print('TEST:' + str(node.left.val))
                    sum_val += node.left.val
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes
        return sum_val
