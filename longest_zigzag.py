# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # maybe something like, 1 + max of longest zigzag path to the left vs to the right? 
        # and when calculating zigzag, keep incrementing the count in the opposite direction of the given? 
        if not root:
            return 0
        
        # return 1 + max(self.zigzag(root, right), self.zigzag(root, left))
        self.ans = 0
    
        # def zigzag(self, node, direction):
        def zigzag(node, direction, length): 
            if not node:
                return 0
            
            self.ans = max(self.ans, length)

            # also could have just had the left vs right indication as a bool lol
            if direction == "right": # last move was right, so need to go left
                # self.ans += max(self.zigzag(node.left, left))
                zigzag(node.left, "left", length + 1)
                # * could also start here as the new zigzag path
                zigzag(node.right, "right", 1)
            else: 
                # self.ans += max(self.zigzag(node.right, right))
                zigzag(node.right, "right", length + 1)
                zigzag(node.left, "left", 1)
            
            # return self.ans
        
        if root: 
            zigzag(root.left, "left", 1)
            zigzag(root.right, "right", 1)
    
        return self.ans