#971. Flip Binary Tree To Match Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        self.flipped = [] # the list of flipped nodes
        self.i = 0 # initialization of the start point order

        def dfs(node): # check if this node is flipped
            if node: # if node is not null
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) && node.left && node.left.val != voyage[self.i]): self.flipped.append(node.val)
                    dfs(node.left)
                    dfs(node.right)

                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
