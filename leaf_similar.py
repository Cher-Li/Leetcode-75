# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        
        # so sorta like, depth first search, whenever reach a leaf, that's the next in the sequence? 
        # we could build both leaf sequences then compare, or build one and match the second? 

        # seq1 = self.dfs(root1, [])
        # seq2 = self.dfs(root2, [])
        seq1 = []
        seq2 = []

        self.dfs(root1, seq1)
        self.dfs(root2, seq2) 

        return seq1 == seq2
    
    def dfs(self, node, sequence): 
        if not node:
            return
        
        # * put this first then return
        if not node.left and not node.right:   
            sequence.append(node.val)
            return 
        
        if node.left:
            self.dfs(node.left, sequence)
        if node.right: # * also if not elif since could have both
            self.dfs(node.right, sequence)
        
        # return sequence