# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        # not exactly rightmost leaf nodes? 
        # like we need a level order traversal, taking the last *valid* node of each level
        # input includes the null values for empty nodes so could just directly do 1 node for level 1, 2 for level 2, 4 for level 3, and so on? 
        # ^ actually no could just append all children after finishing one level and the length would be the size of that level

        result = []

        if not root:
            return [] # * not just None

        # * keep track of all the nodes per level
        queue = deque([root])

        while queue: 
            lvl_size = len(queue) 

            for i in range(lvl_size):
                node = queue.popleft()

                if i == lvl_size - 1: # rightmost node
                    result.append(node.val) # * append the val
                
                # then append the next lvl nodes
                if node.left:
                    queue.append(node.left)
                
                if node.right: 
                    queue.append(node.right)
        
        return result